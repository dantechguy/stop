import json
import sprite

def generate_code(json_string):
    json_dictionary = json.loads(json_string)

    sprites = []

    for target_index in json_dictionary['targets']:
        temporary_sprite = sprite.Sprite(json_dictionary, target_index)
        sprites.append(temporary_sprite)







# generate oop structure
# sprite > scripts > script > block