import tkinter as tk
from . import scratch_math as v
import random
from PIL import Image, ImageTk
import os 

class SpriteCode:
    def __init__(self, parameters):
        self.parameters = parameters
        # private
        self.project =          parameters['project']
        self.canvas =           parameters['canvas']
        self.sprite_container = parameters['sprite_container']
        self.layer_order =      parameters['layer_order']       # number
        self.visible =          parameters['visible']           # true / false
        self.draggable =        parameters['draggable']         # True / False
        self.rotation_style =   parameters['rotation_style']    # Left-Right / Dont Rotate / All Around
        self.costumes =         parameters['costumes']          # dict of name and image dir
        # public
        self.x =                parameters['x']
        self.y =                parameters['y']                                 
        self.direction =        parameters['direction']         # angle -179 to 180
        self.size =             parameters['size']              # percentage 0 to 100
        self.costume_number =   parameters['costume_number']    # index starts 0
        self.volume =           parameters['volume']            # percentage 0 to 100
        # NOT BUILT INS
        # creating canvas image
        self.canvas_img = self.canvas.canvas.create_image((0, 0))
        self.pil_img = None
        self.pil_img_edited = None
        self.tk_img = None
        
        self.update_position()
        self.update_sprite()

    # motion
    def move_steps(self, parameters):  # steps
        steps = parameters[0]
        x = 0
        y = 0
        if self.direction == 0:
            y = steps
        elif self.direction == 90:
            x = steps
        elif self.direction == 180:
            y = 0 - steps
        elif self.direction == -90:
            x = 0 - steps
        else:
            x = steps*v.sin(self.direction)
            y = steps*v.cos(self.direction)
        self.x += x
        self.y += y
        self.update_position()

    def turn_right_degrees(self, parameters):  # degrees
        degrees = parameters[0]
        self.direction += degrees
        self.update_sprite()

    def turn_left_degrees(self, parameters):  # degrees
        degrees = parameters[0]
        self.direction -= degrees
        self.update_sprite()

    def go_to(self, parameters):  # option
        option = parameters[0]
        if option == "random_position":
            x = random.randint(-240, 240)
            y = random.randint(-180, 180)
        elif option == "mouse_pointer":
            # use system to find mouse coordinates
            x = None
            y = None
        else:
            # use system to find other sprite coordinates
            sprite = self.main.sprites[option]
            x = sprite.x
            y = sprite.y
        self.x = x
        self.y = y
        self.update_position()

    def go_to_x_y(self, parameters):  # x, y
        self.x = parameters[0]
        self.y = parameters[1]
        self.update_position()

    def glide_secs_to(self, parameters):  # option, seconds
        option = parameters[0]
        seconds = parameters[1]
        if option == "random_position":
            x = random.randint(-240, 240)
            y = random.randint(-180, 180)
        elif option == "mouse_pointer":
            # use system to find mouse coordinates
            x = None
            y = None
        else:
            # use system to find other sprite coordinates
            x = None
            y = None
        self.x = x
        self.y = y

    def glide_secs_to_x_y(self, parameters):  # x, y
        # work - do replace 'glide' with a 'for loop + goto'
        self.x = parameters[0]
        self.y = parameters[1]

    def point_in_direction(self, parameters):  # direction
        self.direction = parameters[0]
        self.update_sprite()

    def point_towards(self, parameters):  # option
        option = parameters[0]
        if option == "mouse_pointer":
            # use system to find mouse coordinates
            target_x = None
            target_y = None
        else:
            # use system to find other sprite coordinates
            target_x = None
            target_y = None
        x = target_x - self.x
        y = target_y - self.y
        angle = (y / x).atan()
        self.direction = angle

    def change_x_by(self, parameters):  # x
        self.x += parameters[0]
        self.update_position()

    def set_x_to(self, parameters):  # x
        self.x = parameters[0]
        self.update_position()

    def change_y_by(self, parameters):  # y
        self.y += parameters[0]
        self.update_position()

    def set_y_to(self, parameters):  # y
        self.y = parameters[0]
        self.update_position()

    def if_on_edge_bounce(self, parameters): # not straightforward
        pass

    def set_rotation_style(self, parameters):  # option
        option = parameters[0]
        self.rotation_style = option

    # looks
    def say_for_seconds(self, parameters): # use global function?
        pass

    def say(self, parameters):
        pass

    def think_for_seconds(self, parameters):
        pass

    def think(self, parameters):
        pass

    def switch_costume_to(self, parameters):  # costume
        costume = parameters[0]
        if type(costume) == "int":
            self.switch_costume_to_num(costume)
        elif type(costume) == "str":
            try:
                self.switch_costume_to_str(costume)
            except ValueError:
                self.switch_costume_to_num(int(float(costume)))
        self.update_sprite()

    def next_costume(self, parameters):
        self.costume_number += 1
        if self.costume_number > len(self.costumes)-1:
            self.costume_number = 0
        self.update_sprite()

    def change_size_by(self, parameters):  # percentage
        percentage = parameters[0]
        new_size = (self.size + percentage, )
        self.set_size_to(new_size)

    def set_size_to(self, parameters):  # percentage
        percentage = parameters[0]
        self.size = percentage
        if self.size < 1:
            self.size = 1
        self.update_sprite()

    def change_look_effect_by(self, parameters): # effect name, value
        pass

    def set_look_effect_to(self, parameters): #effect name, value
        pass

    def clear_graphic_effects(self, parameters):
        pass

    def show(self, parameters):
        self.visible = True
        self.update_sprite()

    def hide(self, parameters):
        self.visible = False
        self.update_sprite()

    def go_to_layer(self, parameters): # front/back
        pass

    def go_layers(self, parameters): # forward/backward, number of layers
        pass

    # sound
    def play_sound_until_done(self, parameters): #sound name
        pass

    def play_sound(self, parameters): # sound name
        pass

    def change_sound_effect_by(self, parameters): # pitch/pan left-right, value
        pass

    def set_sound_effect_to(self, parameters): # pitch/pan left-right, value
        pass

    def clear_sound_effects(self, parameters):
        pass

    def change_volume_by(self, parameters): # percentage
        pass

    def set_volume_to(self, paramters): # percentage
        pass




    ### NOT BUILT INS ###

    def bind_click(self):
        self.canvas.canvas.tag_bind(self.canvas_img, '<Button-1>', self.sprite_clicked)

    def sprite_clicked(self):
        self.project.send_sprite_clicked_event(self.sprite_container)


    def find_index_of_dictionary_in_list_with_key_that_has_value(self, list_of_dictionaries, key, value):
        for index, dictionary in enumerate(list_of_dictionaries):
            if dictionary[key] == value:
                return index
        raise ValueError

    def switch_costume_to_str(self, costume):
        costume_dictionary_index = self.find_index_of_dictionary_in_list_with_key_that_has_value(self.costumes, "name", costume)
        index = costume_dictionary_index+1
        self.costume_number = index

    def switch_costume_to_num(self, costume):
        if costume in range(len(self.costumes)):
            self.costume_number = costume
        else:
            self.costume_number = costume % len(self.costumes)

    def update_position(self):
        x = self.x + 240
        y = 180 - self.y
        self.canvas.canvas.coords(self.canvas_img, x, y)

    def update_size(self):
        multiplier = self.size * 0.01
        current_width = self.pil_img.size[0]
        current_height = self.pil_img.size[1]
        new_width = current_width*multiplier
        new_height = current_height*multiplier
        new_size = (int(float(new_width)), int(float(new_height)))
        self.pil_img_edited = self.pil_img.resize(new_size)

    def update_costume(self):
        self.pil_img = Image.open(self.costumes[int(self.costume_number)-1]["file"])


    def update_rotation(self):
        if self.rotation_style == "all around":
            self.pil_img_edited = self.pil_img_edited.rotate(int(0-self.direction)+90, expand=1, resample=Image.BICUBIC)
        elif self.rotation_style == "dont rotate":
            pass
        elif self.rotation_style == "left-right":
            if self.direction < 0:
                self.pil_img_edited = self.pil_img_edited.transpose(Image.FLIP_LEFT_RIGHT)

    def update_sprite(self):
        if self.visible:
            self.update_costume()
            self.update_size()
            self.update_rotation()
            self.tk_img = ImageTk.PhotoImage(self.pil_img_edited)
            self.canvas.canvas.itemconfig(self.canvas_img, image=self.tk_img, state="normal")
        else:
            self.canvas.canvas.itemconfig(self.canvas_img, state="hidden")
            


