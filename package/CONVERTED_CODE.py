import stop
project = stop.Project()

class class_Sprite1(stop.Sprite):
    def __init__(self, project, *args):
        super().__init__(project, args[0])
        project.events.add_key_pressed_event('space', self.key_pressed_0)
        project.events.add_key_pressed_event('left', self.key_pressed_1)
        project.events.add_key_pressed_event('right', self.key_pressed_2)
        project.events.add_green_flag_event(self.green_flag_0)
        project.events.add_green_flag_event(self.green_flag_1)
        project.events.add_green_flag_event(self.green_flag_2)
        project.events.add_green_flag_event(self.green_flag_3)
        project.events.add_green_flag_event(self.green_flag_4)


    def key_pressed_0(self):
        self.move_steps(15)


    def key_pressed_1(self):
        self.turn_left_degrees(15)


    def key_pressed_2(self):
        self.turn_right_degrees(15)


    def green_flag_0(self):
        project.wait(33)
        self.switch_costume_to('ghoul-a')
        self.play_sound('zoop')


    def green_flag_1(self):
        for i in range(10):
            self.play_sound('203-starlight-carnival-act-1.mp3')
            project.wait()


    def green_flag_2(self):
        self.switch_costume_to('costume1')


    def green_flag_3(self):
        self.go_to_x_y(5, -6)


    def green_flag_4(self):
        while True:
            self.change_look_effect_by('color', 50)
            project.wait()

sprite_class_ = class_Sprite1(project, {'layer_order': 1,
    'visible': True,
    'draggable': False,
    'rotation_style': 'all around',
    'costumes': [{'name': 'costume1',
    'file': 'assets/bcaaa8547a07cfe572c0967ba829e99d.png',
    'rotation_x': 47,
    'rotation_y': 55},
    {'name': 'ghoul-a',
    'file': 'assets/4447af48f4f2704c4ff2677f4d14872c.png',
    'rotation_x': 75,
    'rotation_y': 75}],
    'x': 115.13811664435866,
    'y': -73.47650271557009,
    'size': 100,
    'direction': 45,
    'costume_number': 1,
    'volume': 100})


class class_Sprite2(stop.Sprite):
    def __init__(self, project, *args):
        super().__init__(project, args[0])
        project.events.add_green_flag_event(self.green_flag_0)
        project.events.add_green_flag_event(self.green_flag_1)


    def green_flag_0(self):
        self.go_to_x_y(131, -139)
        while True:
            self.turn_right_degrees(15)
            project.wait()

    def green_flag_1(self):
        while True:
            self.change_look_effect_by('color', -50)
            project.wait()

sprite_class_ = class_Sprite2(project, {'layer_order': 2,
    'visible': True,
    'draggable': False,
    'rotation_style': 'all around',
    'costumes': [{'name': 'photo1',
    'file': 'assets/02a7fbc99462d253130226cd69d9d159.png',
    'rotation_x': 93,
    'rotation_y': 150}],
    'x': 131,
    'y': -139,
    'size': 100,
    'direction': 135,
    'costume_number': 0,
    'volume': 100})


class class_Sprite3(stop.Sprite):
    def __init__(self, project, *args):
        super().__init__(project, args[0])
        project.events.add_green_flag_event(self.green_flag_0)
        project.events.add_green_flag_event(self.green_flag_1)


    def green_flag_0(self):
        self.go_to_x_y(-183, -141)
        while True:
            self.turn_left_degrees(15)
            project.wait()

    def green_flag_1(self):
        while True:
            self.change_look_effect_by('color', -50)
            project.wait()

sprite_class_ = class_Sprite3(project, {'layer_order': 3,
    'visible': True,
    'draggable': False,
    'rotation_style': 'all around',
    'costumes': [{'name': 'photo1',
    'file': 'assets/02a7fbc99462d253130226cd69d9d159.png',
    'rotation_x': 93,
    'rotation_y': 150}],
    'x': -183,
    'y': -141,
    'size': 100,
    'direction': 45,
    'costume_number': 0,
    'volume': 100})

project.run()

    