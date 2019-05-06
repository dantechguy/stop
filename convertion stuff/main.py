import extract_files

def main(sb3Url):
  extract_files.extractFilesAndCreateTempFolder(sb3Url)

  customCode = ''

  finalCode = '''import stop

project = stop.Project()

{0}

project.run()'''.format(customCode)


if __name__ == '__main__':
  sb3Url = 'C:/Users/danie/Documents/code/python/scratch2python/convertion stuff/assets.sb3'
  main(sb3Url)




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