import conversion_tables
from prefs import prefs

class Sprite:
  def __init__(self, sprite_json, all_sprites_json):
    self.sprite_json = sprite_json
    self.all_sprites_json = all_sprites_json

    self.sprite_name = sprite_json['name']
    self.sprite_variable_name = '{0}{1}'.format(
      prefs.sprite_variable_prefix, 
      self.sprite_name
    )


  def generate_code(self):
    costumes = self.sprite_json['costumes']
    costume_code = self.generate_costume_code()

    sprite_creation_code = '{0}{1} = stop.Sprite({2}, costumes={3})'.format(
      prefs.sprite_variable_prefix, 
      self.sprite_name,
      prefs.project_variable_name,
      prefs.init_costume_variable_name
    )

    script_code_container = ScriptContainer(
      self.sprite_json, 
      self.all_sprites_json,
      self.sprite_variable_name
    )
    script_code = script_code_container.generate_code()

    sprite_code = '\n\n'.join([
      costume_code,
      sprite_creation_code,
      script_code
    ])
    return sprite_code


  def generate_costume_code(self):
    costume_json = self.sprite_json['costumes']
    costume_list = []
    for costume in costume_json:
      costume_id = costume['assetId']
      costume_file_directory = '{0}{1}'.format(
        prefs.costume_file_directory, 
        costume_id
      )
      costume_name = costume['name']
      costume_rotate_centre_x = costume['rotationCenterX']
      costume_rotate_centre_y = costume['rotationCenterY']

      costume_dictionary = {
        'file': costume_file_directory,
        'name': costume_name,
        'rotate_centre_x': costume_rotate_centre_x,
        'rotate_centre_y': costume_rotate_centre_y,
      }

      costume_list.append(costume_dictionary)

    costume_code = '{0} = {1}'.format(
      prefs.init_costume_variable_name, 
      costume_list
    )
    return costume_code





class ScriptContainer: # pass all json blocks
  def __init__(self, sprite_json, all_sprites_json, sprite_variable_name):
    self.sprite_json = sprite_json
    self.all_sprites_json = all_sprites_json
    self.sprite_name = sprite_variable_name

    self.blocks = self.generate_blocks() # dict
    blocks_sorted_into_lists = self.sort_blocks(self.blocks)
    self.scripts = [Script(script_list, self.blocks) for script_list in blocks_sorted_into_lists]

  def generate_code(self):
    script_codes = []
    for script in self.scripts:
      script_code = script.generate_code()
      script_codes.append(script_code)

    all_script_code = '\n\n'.join(script_codes)
    return all_script_code

  def generate_blocks(self):
    blocks_json = self.sprite_json['blocks']
    block_objects = {}

    for block_json_key in blocks_json:
      block_json = blocks_json[block_json_key]
      block_id = block_json_key
      block = Block(block_id, block_json, self.sprite_name)

      block_objects[block_id] = block

    return block_objects


  def sort_blocks(self, blocks): # use aboveId and belowId
    blocks_sorted_into_lists = [[blocks[blockId]] for blockId in blocks if blocks[blockId].aboveId == None]

    for block_list in blocks_sorted_into_lists:
      current_block = block_list[0]

      while current_block.belowId != None:
        next_block_id = current_block.belowId
        next_block = blocks[next_block_id]
        block_list.append(next_block)
        current_block = next_block

    return blocks_sorted_into_lists





class Script:
  def __init__(self, list_of_blocks, dict_of_blocks):
    self.dict_of_blocks = dict_of_blocks
    self.list_of_blocks = list_of_blocks

  def generate_code(self):
    block_codes = []
    for block in self.blocks:
      block_code = block.generate_code(dict_of_blocks)
      block_codes.append(block_code)

    all_blocks_code = '\n\n'.join(block_codes)
    return all_blocks_code






class Block: # pass a single json block
  def __init__(self, block_id, block_json, sprite_name):
    self.block_json = block_json
    self.block_id = block_id
    self.sprite_name = sprite_name

    self.opcode = self.find_opcode() # str
    self.aboveId = self.find_above() # str
    self.belowId = self.find_below() # str
    self.inputs = self.find_inputs() # dict

  def generate_code(self, dict_of_blocks):
    unformatted_code = conversion_tables.block_to_code[self.opcode]
    formatted_code = stringFormatDictionary(unformatted_code, self.inputs) ### W O R K  H E R E ###

    # todo: use 'dict_of_blocks' when formatting code to include other blocks's generate_code function return_inputs

    
    return formatted_code

  def find_opcode(self):
    return self.block_json['opcode']

  def find_above(self):
    return self.block_json['parent']

  def find_below(self):
    return self.block_json['next']

  def find_inputs(self):
    input_json = self.block_json['inputs']
    field_json = self.block_json['fields']

    input_values = self.extract_input_values(input_json)
    field_values = self.extract_input_values(field_json)
    sprite_name = {'name':self.sprite_name}

    return {**input_values, **field_values, **sprite_name}

  def extract_input_values(self, input_json):
    return_inputs = {}

    for input_key in input_json:
      first_value = input_json[input_key][0]
      first_value_type = type(first_value).__name__
      second_value = input_json[input_key][1]
      second_value_type = type(second_value).__name__

      if first_value_type == 'str': # is field
        input_value = first_value

      elif second_value_type == 'list': # is value
        input_value = second_value[1]

      elif second_value_type == 'str': # is md5 id
        input_value = second_value

      return_inputs[input_key.lower()] = input_value

    return return_inputs

"""
<md5 id>: {}
  'opcode': <opcode>,
  'inputs': {
    <input name>: [<index>, [<value type>, <value>]],
    <input name>: [<index>, <md5 id>],
  },
  'fields': {
    <field name>: [<choice>, <additional info>]
  },



<value type>:
3 = md5 id
4 = number

10 = string
"""

def stringFormatDictionary(string, dictionary): #
  for key in dictionary:
    findTerm = '{{0}}'.format(key)
    replaceTerm = dictionary[key]
    string.replace(findTerm, replaceTerm)
  return string




spr_json = {'isStage': False, 'name': 'Sprite1', 'variables': {}, 'lists': {}, 'broadcasts': {}, 'blocks': {'EfOy{q7?Pg_vh^HN|+!9': {'opcode': 'motion_glideto', 'next': None, 'parent': None, 'inputs': {'SECS': [1, [4, '1']], 'TO': [3, '|p2Hs!q~bJuEm4DIPu/4', 'sa5r,f[QsY9$(TVESgI]']}, 'fields': {}, 'shadow': False, 'topLevel': True, 'x': 142, 'y': 379}, 'sa5r,f[QsY9$(TVESgI]': {'opcode': 'motion_glideto_menu', 'next': None, 'parent': None, 'inputs': {}, 'fields': {'TO': ['_random_', None]}, 'shadow': True, 'topLevel': True, 'x': 299, 'y': 387}, '|p2Hs!q~bJuEm4DIPu/4': {'opcode': 'operator_letter_of', 'next': None, 'parent': 'EfOy{q7?Pg_vh^HN|+!9', 'inputs': {'LETTER': [1, [6, '1']], 'STRING': [1, [10, 'apple']]}, 'fields': {}, 'shadow': False, 'topLevel': False}}, 'comments': {}, 'currentCostume': 0, 'costumes': [{'assetId': 'b7853f557e4426412e64bb3da6531a99', 'name': 'costume1', 'bitmapResolution': 1, 'md5ext': 'b7853f557e4426412e64bb3da6531a99.svg', 'dataFormat': 'svg', 'rotationCenterX': 48, 'rotationCenterY': 50}, {'assetId': 'e6ddc55a6ddd9cc9d84fe0b4c21e016f', 'name': 'costume2', 'bitmapResolution': 1, 'md5ext': 'e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg', 'dataFormat': 'svg', 'rotationCenterX': 46, 'rotationCenterY': 53}], 'sounds': [{'assetId': '83c36d806dc92327b9e7049a565c6bff', 'name': 'Meow', 'dataFormat': 'wav', 'format': '', 'rate': 48000, 'sampleCount': 40681, 'md5ext': '83c36d806dc92327b9e7049a565c6bff.wav'}], 'volume': 100, 'layerOrder': 1, 'visible': True, 'x': 0, 'y': 0, 'size': 100, 'direction': 90, 'draggable': False, 'rotationStyle': 'all around'}

all_json = {'targets': [{'isStage': True, 'name': 'Stage', 'variables': {'`jEk@4|i[#Fk?(8x)AV.-my variable': ['my variable', 0]}, 'lists': {}, 'broadcasts': {}, 'blocks': {}, 'comments': {}, 'currentCostume': 0, 'costumes': [{'assetId': 'cd21514d0531fdffb22204e0ec5ed84a', 'name': 'backdrop1', 'md5ext': 'cd21514d0531fdffb22204e0ec5ed84a.svg', 'dataFormat': 'svg', 'rotationCenterX': 240, 'rotationCenterY': 180}], 'sounds': [{'assetId': '83a9787d4cb6f3b7632b4ddfebf74367', 'name': 'pop', 'dataFormat': 'wav', 'format': '', 'rate': 48000, 'sampleCount': 1123, 'md5ext': '83a9787d4cb6f3b7632b4ddfebf74367.wav'}], 'volume': 100, 'layerOrder': 0, 'tempo': 60, 'videoTransparency': 50, 'videoState': 'on', 'textToSpeechLanguage': None}, {'isStage': False, 'name': 'Sprite1', 'variables': {}, 'lists': {}, 'broadcasts': {}, 'blocks': {'EfOy{q7?Pg_vh^HN|+!9': {'opcode': 'motion_glideto', 'next': None, 'parent': None, 'inputs': {'SECS': [1, [4, '1']], 'TO': [3, '|p2Hs!q~bJuEm4DIPu/4', 'sa5r,f[QsY9$(TVESgI]']}, 'fields': {}, 'shadow': False, 'topLevel': True, 'x': 142, 'y': 379}, 'sa5r,f[QsY9$(TVESgI]': {'opcode': 'motion_glideto_menu', 'next': None, 'parent': None, 'inputs': {}, 'fields': {'TO': ['_random_', None]}, 'shadow': True, 'topLevel': True, 'x': 299, 'y': 387}, '|p2Hs!q~bJuEm4DIPu/4': {'opcode': 'operator_letter_of', 'next': None, 'parent': 'EfOy{q7?Pg_vh^HN|+!9', 'inputs': {'LETTER': [1, [6, '1']], 'STRING': [1, [10, 'apple']]}, 'fields': {}, 'shadow': False, 'topLevel': False}}, 'comments': {}, 'currentCostume': 0, 'costumes': [{'assetId': 'b7853f557e4426412e64bb3da6531a99', 'name': 'costume1', 'bitmapResolution': 1, 'md5ext': 'b7853f557e4426412e64bb3da6531a99.svg', 'dataFormat': 'svg', 'rotationCenterX': 48, 'rotationCenterY': 50}, {'assetId': 'e6ddc55a6ddd9cc9d84fe0b4c21e016f', 'name': 'costume2', 'bitmapResolution': 1, 'md5ext': 'e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg', 'dataFormat': 'svg', 'rotationCenterX': 46, 'rotationCenterY': 53}], 'sounds': [{'assetId': '83c36d806dc92327b9e7049a565c6bff', 'name': 'Meow', 'dataFormat': 'wav', 'format': '', 'rate': 48000, 'sampleCount': 40681, 'md5ext': '83c36d806dc92327b9e7049a565c6bff.wav'}], 'volume': 100, 'layerOrder': 1, 'visible': True, 'x': 0, 'y': 0, 'size': 100, 'direction': 90, 'draggable': False, 'rotationStyle': 'all around'}], 'monitors': [], 'extensions': [], 'meta': {'semver': '3.0.0', 'vm': '0.2.0-prerelease.20190430163103', 'agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}}

sprite = Sprite(spr_json, all_json)
print(sprite.generate_code())