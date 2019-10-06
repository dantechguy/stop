import block

class Scripts:
    def __init__(self, all_json, target_index):
        self.all_json = all_json
        self.target_index = target_index
        self.sprite_json = json_dictionary['targets'][target_index]

        self.blocks = self.get_blocks()
        self.update_neighbour_block_indexes()
        # self.scripts = self.get_scripts()


    def get_blocks(self):
        block_dictionary = {}
        for block_md5 in self.sprite_json['blocks']:
            block_json = self.sprite_json['blocks'][block_md5]
            temporary_block = block.Block(self.all_json, self.target_index, self.block_md5)
            block_dictionary[block_md5] = temporary_block
        return block_dictionary


    def update_neighbour_block_indexes(self):
        for block_md5 in self.blocks:
            temporary_block = self.blocks[block_md5]
            temporary_block.block_dictionary = self.blocks
            temporary_block.update_neighbour_block_indexes(self.blocks)

    def get_scripts(self):
        for block_md5 in self.blocks:
            temporary_block = self.blocks[block_md5]
            if temporary_block.above_block == None: # is top level block
                script_code = temporary_block.generate_script_code() # makes all code below

