from kivy.clock import Clock

from . import config
import decev

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.graphics import Color, Rectangle, Translate


class ScratchApp(App):
    def __init__(self):
        super().__init__()
        self.widget = Widget(size=config.window.size)
        self.widget.bind(on_touch_up=lambda w, t: print('touch:', t))
        with self.widget.canvas:
            Color(1, 1, 1)
            Rectangle(pos=(0, 0), size=config.window.size)
            # Translate(*config.window.origin)

    def build(self):
        self.icon = 'favicon.ico'
        self.title = config.window.title
        return self.widget


class Project:
    def __init__(self,
                 width=config.window.width,
                 height=config.window.height):
        self.width = width
        self.height = height
        self.mouse = (0, 0)

        self.event = decev.EventHandler()

        Config.set('graphics', 'maxfps', config.window.fps)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', self.width)
        Config.set('graphics', 'height', self.height)

        from kivy.core.window import Window
        def mouse_move(w, pos):
            self.mouse = tuple(map(int, pos))
            self.event.run('mouse_move')
        Window.bind(mouse_pos=mouse_move)

        self.app = ScratchApp()

    def run(self):
        Clock.schedule_once(lambda dt: self.event.run('green_flag'))
        self.app.run()

