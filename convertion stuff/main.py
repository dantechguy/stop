import json, tkinter as tk, os
import file_setup, msplit # ,json_to_python

# get sb3 file
target_sb3_file_dir = file_setup.open_file("Open", [("Scratch Files", "*.sb3")])
if target_sb3_file_dir == "":
    exit()

# initialising variables
project_name = msplit.msplit(target_sb3_file_dir, ["\\", "/"]).replace(".sb3", "")
project_data_dir = "project_data"
assets_file_dir = "assets/"

# file setup
file_setup.remove_assets_folder(assets_file_dir)
file_setup.unzip_sb3_file_to_assets(target_sb3_file_dir, assets_file_dir)

# extracting json data
json_data = file_setup.read_json(assets_file_dir + "project.json")
targets = json_data["targets"]

# convert json sb3 to python
sprites = []
for i in targets:
    print(i)
    # name = sprite[""]
    # json_to_python.sprite()