import stop

project = stop.Project()

class Sprite1(stop.Sprite):
    def __init__(self, project, **kwargs):
        super().__init__(project, **kwargs)
        self.variable_hi = 1

    def walk_and_turn(self):
        while True:
            self.point_towards('mouse_pointer')
            self.move_steps(10)
            self.next_costume()
            project.wait()

sprite1 = Sprite1(project, rotation_style='all around')

project.green_flag(sprite1.walk_and_turn)

project.run()