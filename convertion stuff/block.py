import convertion_tables
from dict_string_format import dict_string_format

class Block:
    def __init__(self, all_json, target_index, block_md5):
        self.all_json = all_json
        self.target_index = target_index
        self.sprite_json = all_json['targets'][self.target_index]
        self.block_md5 = block_md5
        self.block_json = self.sprite_json['blocks'][self.block_md5]
        self.block_dictionary = None

        self.opcode = self.find_opcode()
        self.top_level = self.find_top_level()
        self.indented = self.find_if_indented() # if the block is to be indented
        self.above_block_id = self.find_above_block_id()
        self.above_block = None
        self.below_block_id = self.find_below_block_id()
        self.below_block = None
        self.inputs = self.find_inputs()


    def generate_script_code(self, indent_level):
        unformatted_code = convertion_tables.block_to_code[self.opcode]['code']
        formatted_code = self.fill_in_code_inputs(unformatted_code, indentation)
        if self.indented:
            indentation = prefs.indent * indent_level
        else:
            indentation = ''
        this_block_code = ''.join(indentation, formatted_code)
        if self.below_block != None: # there are blocks below
            below_blocks_code = self.below_block.generate_script_code(indent_level)

        script_code = '\n'.join(this_block_code, below_block_code)
        return script_code

    def fill_in_code_inputs(code, indent_level):
        for key in self.inputs:
            find_term = '{{0}}'.format(key)
            replace_term = self.inputs[key]
            if type(replace_term).__name__ == 'list': # is md5 code
                block_id = replace_term[0]
                temporary_block = self.block_dictionary[block_id]
                below_blocks_code = temporary_block.generate_script_code(indent_level+1) # recursively generate code
                replace_code = block_code
            code.replace(find_term, replace_term)
        return code

    def update_neighbour_block_indexes(self): # is called externally afterwards
        self.above_block = self.block_dictionary[self.above_block_id]
        self.below_block = self.block_dictionary[self.below_block_id]

    def find_opcode(self):
        return self.block_json['opcode']

    def find_top_level(self):
        return self.block_json['topLevel']

    def find_if_indented(self): # if this block is indented or inline
        return self.block_json[self.opcode]['indent']

    def find_above_block_id(self):
        above_block_id = self.block_json['parent']

    def find_below_block_id(self):
        above_block_id = self.block_json['next']

    def find_inputs(self):
        input_json = self.block_json['inputs']
        field_json = self.block_json['fields']

        input_values = self.extract_input_values(input_json)
        field_values = self.extract_input_values(field_json)
        other_values = {'project': prefs.project_variable_name}

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
                input_value = [second_value] # make it a list, so you know its an md5 value

            return_inputs[input_key.lower()] = input_value

        return return_inputs


"""

<md5 id>: {
  'opcode': <opcode>,
  'inputs': {
    <input name>: [<index>, [<value type>, <value>]],
    <input name>: [<index>, <md5 id>],
  },
  'fields': {
    <field name>: [<choice>, <additional info>]
  },
}


<value type>:
3 = md5 id
4 = number

10 = string




"EfOy{q7?Pg_vh^HN|+!9": {
    "shadow": false,
    "next": null,
    "inputs": {
        "SECS": [
            1,
            [
                4,
                "1"
            ]
        ],
        "TO": [
            3,
            "|p2Hs!q~bJuEm4DIPu/4",
            "sa5r,f[QsY9$(TVESgI]"
        ]
    },
    "opcode": "motion_glideto",
    "y": 379,
    "x": 142,
    "topLevel": true,
    "parent": null,
    "fields": {}
}

