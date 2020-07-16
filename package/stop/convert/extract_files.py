# converter - provide a .sb3 file
import zipfile
from .prefs import prefs
import PIL
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

def extract_files_and_create_assets_folder():

    code_file_url = '{0}{1}'.format(
        prefs['output_folder_url'], 
        prefs['code_file_name'])
    assets_folder_url = '{0}{1}'.format(
        prefs['output_folder_url'], 
        prefs['assets_folder_name'])

    unzip(prefs['sb3_url'], assets_folder_url)

    for filename in os.listdir(assets_folder_url):
        if filename.endswith('.svg'):
            file_url = '{0}/{1}'.format(assets_folder_url, filename)
            png_file_url = '{0}/{1}'.format(assets_folder_url, filename.replace('.svg', '.png'))
            
            drawing = svg2rlg(file_url)
            scale = 10
            drawing.width, drawing.height = drawing.minWidth() * scale, drawing.height * scale
            drawing.scale(scale, scale)
            renderPM.drawToFile(drawing, png_file_url, fmt="PNG")


def unzip(start, finish):
    with zipfile.ZipFile(start, "r") as zip_ref:
        zip_ref.extractall(finish)
