from kivy.animation import Animation
import math

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.graphics import Rectangle, Color


class TappableImage(Image):
    def __init__(self, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.callback()


class KivySprite:
    def __init__(self, parent_widget):
        self._parent_widget = parent_widget
        self._scatter_widget = Scatter(#self._tapped,  # callbacks on all areas
                                               do_rotation=False,
                                               do_scale=False,
                                               do_translation=True)
        self._image_widget = Image(source='a.png')
        self._scatter_widget.add_widget(self._image_widget)
        self._parent_widget.add_widget(self._scatter_widget)

        with self._scatter_widget.canvas.before:
            Color(1,0,0)
            Rectangle(pos=self._scatter_widget.pos, size=self._scatter_widget.size)

        self.layer = None
        self.visible = True
        self.rotation_style = 'all around'

        self._scatter_widget.bind(pos=lambda w, p: self._moved())
        self._image_widget.bind(on_touch_down=lambda w, t: self._tapped())

    # to be overriden by Sprite
    def _tapped(self): pass
    def _moved(self): pass
    def _rotated(self): pass
    def _sized(self): pass

    @property
    def image(self):
        return self._image_widget.source

    @image.setter
    def image(self, value):
        self._image_widget.source = value

    @property
    def position(self):
        return self._scatter_widget.pos

    @position.setter
    def position(self, value):
        self._scatter_widget.pos = value

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, value):
        self._scatter_widget.pos = value - (self._image_widget.size[0]/2), self.y

    @property
    def y(self):
        return self.position[1]

    @y.setter
    def y(self, value):
        self._scatter_widget.pos = self.x, value - (self._image_widget.size[1]/2)

    @property
    def size(self):
        return self._scatter_widget.scale * 100

    @size.setter
    def size(self, value):
        self._scatter_widget.scale = value * 0.01

    @property
    def direction(self):
        return (((self._scatter_widget.rotation + 90) + 179) % 360) - 179

    @direction.setter
    def direction(self, value):
        self._scatter_widget.rotation = value - 90

    @property
    def draggable(self):
        return self._scatter_widget.do_translation

    @draggable.setter
    def draggable(self, value):
        self._scatter_widget.do_translation = value

    def glide(self, x, y, time=None):  # either x, y, time or sprite, time
        if time is None:
            time = y
            y = x.y
            x = x.x
        anim = Animation(x=x, y=y, duration=time)
        anim.start(self._scatter_widget)

    def move(self, steps):
        self.x += steps * math.sin(math.radians(self.direction))
        self.y += steps * math.cos(math.radians(self.direction))
        self._moved()

    def point_towards(self, x, y=None):  # test
        if y is None:  # x is a sprite
            y = x.y
            x = x.x
        dy = y - self.y
        dx = x - self.x
        angle = (-90 if dx < 0 else 90) if dy == 0 else math.degrees(math.atan(dx / dy))
        if dy < 0:
            angle += 180
        self.direction = angle

    def touching(self, other_sprite):
        return self._image_widget.collide_widget(other_sprite._image_widget)
