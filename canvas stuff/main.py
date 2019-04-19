from scratch import *
import time


project = Project(fps=30)

cat = Sprite(project)


# def cat_spins_around():
#     cat.set_size_to(50)
#     cat.go_to_x_y(0, 0)
#     cat.point_in_direction(90)
#     while True:
#         cat.move_steps(10)
#         cat.turn_right_degrees(10)
#         project.wait(0.1)

# project.green_flag(cat_spins_around)


project.run()






# from project import Project
# import sprite_canvas
# import threading
# import time

# def demo_function(project, sprite):
#     while True:
#         time.sleep(0.1)
#         project.queue.put({'function': sprite.turn_right_degrees, 'parameters':{'degrees':10}})
#         project.queue.put({'function': sprite.move_steps, 'parameters':{'steps':10}})


# def Main():
#     project = Project()

#     costumes = [
#         {"file":"c961845e1e162b63693e2f99513b30d0.png", "name":"2"}, 
#         {"file":"51b0fad81a7f8ede9aace40727736015.png", "name":"3"}, 
#         {"file":"015ed9655e882926f9b43e4a805556a3.png", "name":"1"}
#     ]
#     sprite = sprite_canvas.SpriteCanvas(
#         project,                       # project
#         project.canvas_object,         # canvas object
#         "Sprite1",                     # name
#         1,                             # layer order
#         True,                          # visible
#         0,                             # x
#         0,                             # y
#         100,                           # size
#         90,                            # direction
#         False,                         # draggable
#         "all around",                  # rotate style
#         costumes,                      # list of costumes
#         0                              # current costume
#     )

#     a = threading.Thread(target=lambda : demo_function(project, sprite), daemon=True)
#     a.start()

#     project.run()

    


# if __name__ == "__main__":
#     Main()