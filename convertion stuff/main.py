import extract_files
import convert
from prefs import prefs
import os
import shutil

def main(sb3_url):
    extract_files.extract_files_and_create_temp_folder(sb3_url)

    json_project_url = '{0}/{1}/project.json'.format(os.path.dirname(sb3_url), prefs['temp_folder_name'])
    with open(json_project_url, 'r') as f:
        json_string = f.read()

    code = convert.generate_code(json_string)

    with open(prefs['code_file_name'], 'w') as f:
        f.write(code)


if __name__ == '__main__':
    try:
        shutil.rmtree(prefs['temp_folder_name'])
    except:
        pass
    sb3_url = 'C:/Users/danie/Documents/code/python/stop/convertion stuff/assets.sb3'
    main(sb3_url)





# each sprite code segment must consist of something like this:



# first load costumes

# costumes = [
#   {'file': '', 'name': ''},
#   {'file': '', 'name': ''},
#   {'file': '', 'name': ''}
# ]

# # next initiate sprite

# sprite_sprite1 = stop.Sprite(project, costumes=costumes)

# # finally create scripts

# def sprite1_greenflag1():
#   sprite_sprite1.move_steps(10)

# project.green_flag(sprite1_greenflag1)