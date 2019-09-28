import stop

project = stop.Project()

class Sprite1(stop.Sprite):
    def walk_and_turn(self):
        self.turn_right_degrees(100)
        self.move_steps(100)

sprite1 = Sprite1(project)

project.green_flag(sprite1.walk_and_turn)

project.run()