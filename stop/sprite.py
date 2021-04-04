import decev
from .kivy_sprite import KivySprite
import math


class Sprite(KivySprite):
    def __init__(self,
                 project,
                 position=(0,0),
                 direction=90,
                 size=100,
                 visible=True,
                 draggable=True,
                 layer=0,
                 rotation_style='all around',
                 volume=100,
                 costumes={}):

        self.project = project
        super().__init__(self.project.app.widget)
        self.event = decev.EventHandler()

        self._costume_images = []  # index to image
        self._costume_names = []  # index to name
        self._costume_number = 0

        self.position = position
        self.direction = direction
        self.size = size
        self.visible = visible
        self.draggable = draggable
        self.layer = layer
        self.rotation_style = rotation_style
        self.volume = volume
        self.costumes = costumes

    @property
    def costume(self):
        return self.costume_number

    @costume.setter
    def costume(self, value):
        if type(value) is str:
            self.costume_name = value
        elif type(value) is int:
            self.costume_number = value

    @property
    def costume_number(self):
        return self._costume_number

    @costume_number.setter
    def costume_number(self, value):
        if self._costume_images:  # has any costumes
            self._costume_number = value % len(self._costume_images)
            self.image = self._costume_images[self.costume_number]
        else:
            self._costume_number = 0

    @property
    def costume_name(self):
        if self._costume_images:
            return self._costume_names[self.costume_number]
        else:
            return ""

    @costume_name.setter
    def costume_name(self, value):
        try:
            index = self._costume_names.index(value)
            self.costume_number = index
        except ValueError:
            pass

    @property
    def costumes(self):
        return dict(zip)

    @costumes.setter
    def costumes(self, costume_dict: dict):
        self._costume_images = list(costume_dict.values())
        self._costume_names = list(costume_dict.keys())
        self._costume_number = 0
        self.costume_number = 0  # shows image

    def distance_to(self, x, y=None):
        if y is None:
            x = x.x
            y = x.y
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    # override from KivySprite
    def _tapped(self):
        self.event.run('clicked')
        print('clicked', self._image_widget.pos)

    def _moved(self):
        self.event.run('moved')

    def _rotated(self):
        self.event.run('rotated')
        print('rotated')

    def _sized(self):
        self.event.run('sized')
        print('sized')
