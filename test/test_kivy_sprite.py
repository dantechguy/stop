from stop.kivy_sprite import KivySprite
import pytest


class DummyWidget:
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.rotation = 0
        self.scale = 1
        self.do_translation = False


@pytest.fixture
def sprite():
    return KivySprite(DummyWidget())


@pytest.mark.parametrize('coords', [(0, 0), (-15, 47), (240, -180)])
def test_setting_position(sprite, coords):
    sprite.position = coords
    assert sprite.position == coords


@pytest.mark.parametrize('coords', [(0, 0), (-15, 47), (240, -180)])
def test_setting_x_y(sprite, coords):
    sprite.x, sprite.y = coords
    assert (sprite.x, sprite.y) == coords


@pytest.mark.parametrize('coords', [(0, 0), (-15, 47), (240, -180)])
def test_position_changes_x_y(sprite, coords):
    sprite.position = coords
    assert sprite.x == coords[0] and sprite.y == coords[1]


@pytest.mark.parametrize('coords', [(0, 0), (-15, 47), (240, -180)])
def test_x_y_changes_position(sprite, coords):
    sprite.x, sprite.y = coords
    assert sprite.position == coords


@pytest.mark.parametrize('coords', [(0, 0), (-15, 47), (240, -180)])
def test_x_y_iadd(sprite, coords):
    sprite.position = -50, -50
    sprite.x += coords[0]
    sprite.y += coords[1]
    assert sprite.position == (coords[0]-50, coords[1]-50)


@pytest.mark.parametrize('size', [15, 47, 240, 180])
def test_setting_size(sprite, size):
    sprite.size = size
    assert sprite.size == size


@pytest.mark.parametrize('dsize', [0, -15, 47, 240, -180])
def test_size_iadd(sprite, dsize):
    sprite.size = 100
    sprite.size += dsize
    assert sprite.size == 100 + dsize


@pytest.mark.parametrize('direction', [(-90, -90), (0, 0), (-180, 180), (181, -179), (360, 0), (45, 45), (270, -90), (-540, 180), (-179.9, 180.1), (180.1, 180.1)])
def test_setting_direction(sprite, direction):
    sprite.direction = direction[0]
    assert round(sprite.direction, 3) == direction[1]


@pytest.mark.parametrize('ddirection', [(-90, 0), (0, 90), (-180, -90), (181, -89), (360, 90), (45, 135), (270, 0), (-540, -90), (91, -179)])
def test_direction_iadd(sprite, ddirection):
    sprite.direction = 90
    sprite.direction += ddirection[0]
    assert sprite.direction == ddirection[1]


@pytest.mark.parametrize('direction, steps, start, end', [(90, 10, (0, 0), (10, 0)), (45, 30, (-30, 4), (-8.787, 25.213)), (60, 28, (5, 2), (29.249, 16)), (-142, 201, (240, 180), (116.252, 21.610))])
def test_move(sprite, direction, steps, start, end):
    sprite.position = start
    sprite.direction = direction
    sprite.move(steps)
    assert (round(sprite.position[0], 3), round(sprite.position[1], 3)) == (round(end[0], 3), round(end[1], 3))


@pytest.mark.parametrize('position, coords, direction', [((50, 50), (50, 50), 90), ((10, -10), (50, -10), 90), ((-37, -41), (-37, 100), 0), ((1, 3), (0, 3), -90), ((-240, -160), (-240, -180), 180), ((11, -5), (-91, -41), -109.440), ((102, -138), (187, 149), 16.498), ((-25, -124), (-40, -144), -143.130)])
def test_point_towards_x_y(sprite, position, coords, direction):
    sprite.position = position
    sprite.point_towards(*coords)
    assert round(sprite.direction, 3) == direction


@pytest.mark.parametrize('position, coords, direction', [((112, 79), KivySprite(DummyWidget((111, -23))), 180.562)])
def test_point_towards_sprite(sprite, position, coords, direction):
    sprite.position = position
    sprite.point_towards(coords)
    assert round(sprite.direction, 3) == direction