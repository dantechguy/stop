import stop
project = stop.Project()

class class_Sprite1(stop.Sprite):
    def __init__(self, project, *args):
        super().__init__(project, args[0])
        project.events.add_green_flag_event(self.green_flag_0)


    def green_flag_0(self):
        self.move_steps(10)
        for i in range(10):
            self.turn_right_degrees(15)
            self.move_steps(5)
            project.wait()
        self.go_to('random_position'
)
        self.point_towards('mouse_pointer'
)


sprite_class_ = class_Sprite1(project, {'layer_order': 1,
    'visible': True,
    'draggable': False,
    'rotation_style': 'all around',
    'costumes': [{'name': 'costume1',
    'file': 'stop/assets/costume1.png',
    'rotation_x': 48,
    'rotation_y': 50},
    {'name': 'costume2',
    'file': 'stop/assets/costume2.png',
    'rotation_x': 46,
    'rotation_y': 53}],
    'x': 0,
    'y': 0,
    'size': 100,
    'direction': 90,
    'costume_number': 0,
    'volume': 100})

project.run()

    