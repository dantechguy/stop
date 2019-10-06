import prefs
import scripts

class Sprite:
    def __init__(self, json_dictionary, target_index):
        self.all_json = json_dictionary
        self.target_index
        self.json = json_dictionary['targets'][target_index]

        self.attributes = self.get_attributes()

        self.scripts = scripts.Scripts(self.all_json, self.target_index)


    def generate_code(self):
        return ''


    def get_attributes(self):
        attributes = {
                'layer_order':      self.json['layerOrder'], 
                'visible':          self.json['visible'],
                'draggable':        self.json['draggable'],
                'rotation_style':   self.json['rotationStyle'],
                'costumes':         self.get_costumes_list(),
                'x':                self.json['x'],
                'y':                self.json['y'],
                'size':             self.json['size'],
                'direction':        self.json['direction'],
                'costume_number':   self.json['currentCostume'],
                'volume':           self.json['volume'],
            }
        return attributes


    def get_costumes_list(self):
        costumes_list = []
        for costume_json in self.json['costumes']:
            costume_dictionary = {
                'name':         costume_json['name'],
                'file':         '{0}{1}.png'.format(prefs.costume_file_directory, costume_json['assetId']),
                'rotation_x':   costume_json['rotationCenterX'],
                'rotation_y':   costume_json['rotationCenterY']
            }
            costumes_list.append(costume_dictionary)
        return costumes_list



"""
{
    "currentCostume": 0,
    "isStage": false,
    "y": 0,
    "costumes": [],
    "comments": {},
    "direction": 0,
    "variables": {},
    "rotationStyle": "",
    "broadcasts": {},
    "blocks": {},
    "x": 0,
    "draggable": false,
    "visible": true,
    "lists": {},
    "name": "",
    "sounds": [],
    "layerOrder": 1,
    "volume": 100,
    "size": 100
}