from PIL import Image

im = Image.open('tblock/move_steps.png')

px = im.load()

print(px[50,50])