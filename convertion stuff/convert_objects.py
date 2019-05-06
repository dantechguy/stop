import opcode_to_type

class Sprite:
  def __init__(self, sprite_json, all_sprites_json):
    self.sprite_json = sprite_json
    self.all_sprites_json = all_sprites_json

    # variables
    self.sprite_variable_prefix = 's_'
    self.variable_variable_prefix = 'v_'
    self.costume_file_directory = 'assets/' # end with '/'
    self.init_costume_variable_name = 'costumes'
    self.project_variable_name = 'project'

    self.sprite_name = sprite_json['name']
    self.sprite_variable_name = '{0}{1}'.format(
      self.sprite_variable_prefix, 
      self.sprite_name
    )


  def generate_code(self):
    costumes = sprite_json['costumes']
    costume_code = self.generate_costume_code()

    sprite_creation_code = '{0}{1} = stop.Sprite({2}, costumes={3})'.format(
      self.sprite_variable_prefix, 
      self.sprite_name,
      self.project_variable_name,
      self.init_costume_variable_name
    )

    script_code_container = ScriptContainer(
      self.sprite_json, 
      self.all_sprites_json
    )
    script_code = script_code_container.generate_code()

    sprite_code = '\n\n'.join([
      costume_code,
      sprite_creation_code,
      script_code
    ])


  def generate_costume_code(self):
    costume_json = self.sprite_json['costumes']
    costume_list = []
    for costume in costume_json:
      costume_id = costume['assetId']
      costume_file_directory = '{0}{1}'.format(
        self.costume_file_directory, 
        costume_id
      )
      costume_name = costume['name']
      costume_rotate_centre_x = costumeJson['rotationCenterX']
      costume_rotate_centre_y = costumeJson['rotationCenterY']

      costume_dictionary = {
        'file': costume_file_directory,
        'name': costume_name,
        'rotate_centre_x': costume_rotate_centre_x,
        'rotate_centre_y': costume_rotate_centre_y,
      }

      costume_list.append(costume_dictionary)

    costume_code = '{0} = {1}'.format(
      self.init_costume_variable_name, 
      costume_list
    )
    return costume_code



class ScriptContainer: # pass all json blocks
  def __init__(self, sprite_json, all_sprites_json):
    self.sprite_json = sprite_json
    self.all_sprites_json = all_sprites_json


  def generate_code(self):
    blocks = self.generate_blocks() # dict
    blocks_sorted_into_scripts = self.sort_blocks(blocks)


  def generate_blocks(self):
    blocks_json = self.sprite_json['blocks']
    block_objects = {}

    for block_json_key in blocks_json:
      block_json = blocks_json[block_json_key]
      block_id = block_json_key
      block = Block(block_id, block_json)

      block_objects[block.id] = block

    return block_objects


  def sort_blocks(blocks):
    pass






class Script: # pass a list of json blocks, in order
  def __init__(self, list_of_blocks):
    pass



class Block: # pass a single json block
  def __init__(self, block_id, block_json):
    self.block_json = block_json
    self.block_id = block_id

    self.type = self.find_type()     # str
    self.aboveId = self.find_above() # str
    self.belowId = self.find_below() # str
    self.inputs = self.find_inputs() # dict

  def generate_code(self):
    pass

  def find_type(self):
    opcode = self.block_json['opcode']
    self.type = opcode_to_type.opcode_to_type[opcode]

  def find_above(self):
    self.above = self.block_json['parent']

  def find_below(self):
    self.below = self.block_json['next']

  def find_inputs(self):
    input_json = self.block_json['inputs']
    field_json = self.block_json['fields']
    for input_key in input_json:
      input_value = input_json[input_key][1]
      input_value_type = type(input_value).__name__

      if input_value_type == 'list': # is value
        input_value = input_value[1]

      elif input_value_type == 'str': # is md5 id
        pass

      self.inputs[input_key.lower()] = input_value


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