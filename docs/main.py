from PIL import Image
from os import listdir
from os.path import isfile, join


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y
        return Vector(new_x, new_y)

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def values(self):
        return self.x, self.y

    def copy(self):
        return Vector(self.x, self.y)

    def in_boundary(self, top_left_vector, bottom_right_vector):
        x_in_boundary = self.in_boundary(top_left_vector.x, bottom_right_vector.x)
        y_in_boundary = self.in_boundary(top_left_vector.y, bottom_right_vector.y)
        return x_in_boundary and y_in_boundary

    def in_vertical_boundary(self, top, bottom):
        in_boundary = top <= self.y <= bottom
        return in_boundary

    def in_horizontal_boundary(self, left, right):
        in_boundary = left <= self.x <= right
        return in_boundary


def trim_image(pillow_image):
    width, height = pillow_image.width, pillow_image.height

    top_boundary = find_boundary(pillow_image,      Vector(0, 0),               Vector(1, 0),   Vector(0, 1))
    left_boundary = find_boundary(pillow_image,     Vector(0, 0),               Vector(0, 1),   Vector(1, 0))
    bottom_boundary = find_boundary(pillow_image,   Vector(width-1, height-1),  Vector(-1, 0),  Vector(0, -1))
    right_boundary = find_boundary(pillow_image,    Vector(width-1, height-1),  Vector(0, -1),  Vector(-1, 0))
    boundaries = (left_boundary, top_boundary, width-right_boundary, height-bottom_boundary)
    # print()
    # print(width, height)
    # print(boundaries) # for some reason it trims 1 px extra, only when repeating
    cropped_pillow_image = pillow_image.crop(boundaries) # probably an issue with find_boundary
    return cropped_pillow_image


def find_boundary(pillow_image, start_vector, pixel_vector, line_vector):
    image_pixels = pillow_image.load()
    index_vector = start_vector.copy()
    lines_moved = 0
    max_lines_moved = pillow_image.height-1 if (line_vector.x == 0) else pillow_image.width-1
    while lines_moved < max_lines_moved:
        pixels = image_pixels[index_vector.values()]
        alpha = pixels[3]
        if alpha != 0:
            return lines_moved
        index_vector += pixel_vector
        if not index_vector.in_vertical_boundary(0, pillow_image.height-1):
            index_vector.x += line_vector.x
            index_vector.y = start_vector.y
            lines_moved += 1
        if not index_vector.in_horizontal_boundary(0, pillow_image.width-1):
            index_vector.x = start_vector.x
            index_vector.y += line_vector.y
            lines_moved += 1
    return -1

def convert(in_folder, out_folder):
    image_urls = [
        {'in': '{0}{1}'.format(in_folder, f), 'out': '{0}{1}'.format(out_folder, f)}
        for f in listdir(in_folder) if isfile(join(in_folder, f))]

    print('{0} - {1}'.format(in_folder, out_folder))
    for index, image_url_dict in enumerate(image_urls):
        in_url = image_url_dict['in']
        out_url = image_url_dict['out']
        pillow_image = Image.open(in_url)
        trimmed_image = trim_image(pillow_image)
        size = trimmed_image.size
        scale = 0.75
        resize = (int(size[0]*scale), int(size[1]*scale))
        resized_image = trimmed_image.resize( resize )
        resized_image.save(out_url)
        print('[{0}]'.format('#'*index+' '*(len(image_urls)-1-index)), end='\r')
    print()

convert('./blocks/', './tblocks/')
convert('./scripts/', './tscripts/')
