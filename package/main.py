import stop

project = stop.Project()

class Sprite1(stop.Sprite):
    def __init__(self, project, **kwargs):
        super().__init__(project, **kwargs)
        project.events.add_green_flag_event(self.walk_and_turn)
        project.events.add_key_pressed_event('a', self.left)


    def walk_and_turn(self):
        while True:
            self.point_towards('mouse_pointer')
            if project.interface.key_pressed('space'):
                self.change_x_by(10)
            if project.interface.mouse_down():
                self.move_steps(10)
            project.wait()

    def left(self):
        self.change_x_by(-50)

sprite1 = Sprite1(project, rotation_style='all around', x=-50)

project.run()