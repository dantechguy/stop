import extract_files
from prefs import prefs

def main(sb3_url):
  temp_folder_name = prefs.temp_folder_name
  extract_files.extract_files_and_create_temp_folder(sb3_url, temp_folder_name)

  custom_code = ''

  final_code = '''import stop

{0} = stop.Project()

{1}

{0}.run()'''.format(prefs.project_variable_name, custom_code)


if __name__ == '__main__':
  sb3_url = 'C:/Users/danie/Documents/code/python/scratch2python/convertion stuff/assets.sb3'
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