import stop
import time

project = stop.Project()

sprite = stop.Sprite(project)
sprite.set_size_to(25)

def move_and_turn():
    while True:
        sprite.move_steps(10)
        sprite.turn_right_degrees(10)
        sprite.next_costume()

project.green_flag(move_and_turn)

project.run()