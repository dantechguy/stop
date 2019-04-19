import tkinter as tk
from fluid_var import fv
import random
import math
import time
import threading
import queue

import sprite_canvas


class CanvasObject:
    def __init__(self):
        self.root = tk.Tk()
        self.width = 480
        self.height = 360
        self.origin = (int(self.width/2), int(self.height/2))
        self.root.title("scratch.py library demo")
        self.root.resizable(False, False)
        # init
        self.frame_rate = 2
        self.root.iconbitmap("../favicon.ico")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="#fff", highlightthickness=0)
        self.canvas.pack()

    def run(self):
        self.root.mainloop()




# root = tk.Tk()
# canv = CanvasObject(root)




# def func():
#     for i in range(10):
#         print(i)
#         time.sleep(1)



# thread1 = threading.Thread(target=func, daemon=True) 

# thread1.start()


# canv.run() 

