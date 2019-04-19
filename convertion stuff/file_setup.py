import os, json, shutil, zipfile, tkinter.filedialog as tkfd, tkinter as tk

def open_file(title, filetypes):
    root = tk.Tk()
    icon = tk.PhotoImage(file="favicon.png")
    root.tk.call("wm", "iconphoto", root, "-default", icon)
    root.withdraw()
    target_file = tkfd.askopenfilename(
        title=title,
        filetypes=filetypes
        )
    return target_file

def remove_assets_folder(assets_file_dir):
    if os.path.exists(assets_file_dir):
        for file in os.listdir(assets_file_dir):
            file_path = assets_file_dir + file
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

def unzip_sb3_file_to_assets(sb3_file_target, assets_file_dir):
    with zipfile.ZipFile(sb3_file_target, "r") as zip_ref:
        zip_ref.extractall(assets_file_dir)

def read_json(file_dir):
    with open(file_dir, "r") as f:
        file_data = f.read()
        return json.loads(file_data)


