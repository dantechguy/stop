
# S.To.P (Scratch To Python)

## Intro
*What is [Scratch](https://scratch.mit.edu)?*
A drag and drop, block based programming language aimed at children

*What is [Python](https://python.org)?*
A text based programming language

*Who is this library for?*
Those who know Scratch, and are looking to move on to Python

## Getting Started
Install via PIP:

`python3 -m pip install stop`

Create a new project (and window), and a sprite:

 ```python
 import stop
 project = stop.Project()
 sprite = stop.Sprite(project)
 ```
 
## Documentation
- [stop.project](#project-class)
  - [wait](#stopprojectwait)
  - [switch_backdrop_to](#stopprojectswitch_backdrop_to)
  - [next_backdrop](#stopprojectnext-backdrop)
- [stop.sprite](#sprite-class)
  - [move_steps](#stopspritemove_steps)
  - [turn_right_degrees](#stopspriteturn-right-degrees)
  - [turn_left_degrees](#stopspriteturn-left-degrees)
  - [go_to](#stopsprit.go_to)
  - [go_to_x_y](#stopspritego-to-x-y)
  - [glide_secs_to](#stopspriteglide-secs-to)
  - [glide_secs_x_y](#stopspriteglide_secs-x-y)
  - [point_in_direction](#stopspritepoint-in-direction)
  - [point_towards](#stopspritepoint-towards)
  - [change_x_by](#stopspritechange-x-by)
  - [set_x_to](#stopspriteset-x-to)
  - [change_y_by](#stopspritechange-y-by)
  - [set_y_to](#stopspriteset-y-to)
  - [if_on_edge_bounce](#stopspriteif-on-edge-bounce)
  - [set_rotation_style](#stopspriteset-rotation-style)
  - [say_for_seconds](#stopspritesay-for-seconds)
  - [say](#stopspritesay)
  - [think_for_seconds](#stopspritethink-for-seconds)
  - [think](#stopspritethink)
  - [switch_costume_to](#stopspriteswitch-costume-to)
  - [next_costume](#stopspritenext-costume)
  - [change_size_by](#stopspritechange-size-by)
  - [set_size_to](#stopspriteset-size-to)
  - [show](#stopspriteshow)
  - [hide](#stopspritehide)
- [stop.math](#scratch-maths)

## Project Class
### Create Project Object:
```python
project = stop.Project(
  fps=60
)
```
Optional:
`fps` - Changes project's frame rate if specified.

### Methods

#### stop.project.wait

Pauses the current script for a given amount of time.

```python
stop.project.wait(
  seconds=False
)

# EXAMPLE
project.wait() # waits one frame
project.wait(1) # waits one second
```
Optional:
`seconds` - If 'false' it will wait one frame, otherwise it will wait the time specified in seconds.

<br>

#### stop.project.switch_backdrop_to

Changes the background image, to a given one.

```python
stop.project.switch_backdrop_to(
  backdrop
)

# EXAMPLE
project.switch_backdrop_to("space") # tries to switch to backdrop with name 'space'
prohect.switch_backdrop_to(4) # tries to switch backdrop to backdrop at index 4
```
Required:
`backdrop` - Can be one of:
- `[an integer]` - Switches to the backdrop with the index of the integer given. If integer is out of range of backdrop indexes, it loops around (using modulo).
- `[a string]` - Switches to the backdrop with the name of the string given. If no backdrop has that name, it tries to use the string as an index for a backdrop. If string is not an integer, the backdrop doesn't change.

<br>

#### stop.project.next_backdrop

Changes the background image to the next index.

```python
stop.project.next_backdrop()

# EXAMPLE
project.next_backdrop() # switches to the next backdrop
```

<br>

## Sprite Class
### Create Sprite Object:
```python
sprite= stop.Sprite(
  project
)
```
Required:
`project` - The associated project object, which the sprite will be in.

### Methods
#### stop.sprite.move_steps

Moves the sprite 'forward' in the direction it is facing.

```python
stop.sprite.move_steps(
  steps
)

# EXAMPLE
sprite.move_steps(10) # moves sprite 10 steps
```
Required:
`steps` - Number of pixels the sprite will move in the current direction.

<br>

#### stop.sprite.turn_right_degrees

Turns the sprite to the right.

```python
stop.sprite.turn_right_degrees(
  degrees
)

# EXAMPLE
sprite.turn_right_degrees(90) # turns sprite 90 degrees right
```
Required:
`degrees` - Number of degrees that the sprite will turn to the right.

<br>

#### stop.sprite.turn_left_degrees

Turns the sprite to the left.

```python
stop.sprite.turn_left_degrees(
  degrees
)

# EXAMPLE
sprite.turn_left_degrees(90) # turns sprite 90 degrees left
```
Required:
`degrees` - Number of degrees that the sprite will turn to the left.

<br>

#### stop.sprite.go_to

Moves the sprite to a given location.

```python
stop.sprite.go_to(
  option
)

# EXAMPLE
sprite.go_to("random_position") # moves sprite to random position
sprite.go_to("mouse_pointer") # moves sprite to mouse pointer
sprite.go_to(sprite2) # moves 'sprite' to 'sprite2'
```
Required:
`option` - Can be one of:
- `"random_position"` - Moves the sprite to a random position.
- `"mouse_pointer"` - Moves the sprite to the mouse pointer.
- `[reference to sprite]` - Moves the sprite to the sprite provided.

<br>

#### stop.sprite.go_to_x_y

Moves the sprite to a given x-y coordinate.

```python
stop.sprite.go_to_x_y(
  x,
  y
)

# EXAMPLE
sprite.go_to_x_y(100, -200) # moves the sprite to (100, -200)
```
Required:
`x` - The x-coordinate of where the sprite will go.
`y` - The y-coordinate of where the sprite will go.

<br>

#### stop.sprite.glide_secs_to

The sprite slowly 'glides' to a given location over the duration of a specified amount of time.

```python
stop.sprite.glide_secs_to(
  option,
  seconds
)

# EXAMPLE
sprite.glide_secs_to("random_position", 2) # glides sprite to random position over 2 seconds
sprite.glide_secs_to("mouse_pointer", 3) # glides sprite to mouse pointer over 3 seconds
sprite.glide_secs_to(sprite2, 4) # glides sprite to 'sprite2' over 4 seconds
```
Required:
`option` - Can be one of:
- `"random_position"` - Glides the sprite to a random position.
- `"mouse_pointer"` - Moves the sprite to the mouse pointer.
- `[reference to sprite]` - Moves the sprite to the sprite provided.

`seconds` - How long it takes the sprite to glide there.

<br>

#### stop.sprite.glide_secs_x_y

The sprite slowly 'glides' to a given x-y coordinate over the duration of a specified amount of time.

```python
stop.sprite.glide_secs_x_y(
  x,
  y,
  seconds
)

# EXAMPLE
sprite.glide_secs_to(40, -100, 2) # glides sprite to (40, -100) over 2 seconds
```
Required:
`x` - The x-coordinate of where the sprite will go.
`y` - The y-coordinate of where the sprite will go.
`seconds` - How long it takes the sprite to glide there.

<br>

#### stop.sprite.point_in_direction

Turns the sprite to a given direction, in degrees.

```python
stop.sprite.point_in_direction(
  degrees
)

# EXAMPLE
sprite.point_in_direction(135) # points the sprite to direction 135 degrees
```
Required:
`degrees` - The angle that the sprite will point in degrees.

<br>

#### stop.sprite.point_towards

Points the sprite towards a given object, either the mouse or another sprite.

```python
stop.sprite.point_towards(
  option
)

# EXAMPLE
sprite.point_towards("mouse_pointer") # points the sprite towards the mouse pointer
sprite.point_towards(sprite2,) # points the sprite towards 'sprite2'
```
Required:
`option` - Can be one of:
- `"mouse_pointer"` - Sets the direction of the sprite so that it is facing the mouse pointer.
- `[reference to sprite]` - Sets the direction of the sprite so that it is facing the sprite provided.

<br>

#### stop.sprite.change_x_by

Changes the sprite's x-coordinate by a given amount.

```python
stop.sprite.change_x_by(
  x
)

# EXAMPLE
sprite.change_x_by(-50) # moves the sprite left 50 pixels
```
Required:
`x` - How many pixels to change the sprite's x-coordinate by.

<br>

#### stop.sprite.set_x_to

Sets the sprite's x-coordinate to a given value.

```python
stop.sprite.set_x_to(
  x
)

# EXAMPLE
sprite.set_x_to(200) # moves the sprite to x-coordinate 200
```
Required:
`x` - What to set the sprite's x-coordinate to

<br>

#### stop.sprite.change_y_by

Changes the sprite's y-coordinate by a given amount.

```python
stop.sprite.change_y_by(
  x
)

# EXAMPLE
sprite.change_y_by(-60) # moves the sprite down 60 pixels
```
Required:
`x` - How many pixels to change the sprite's y-coordinate by.

<br>

#### stop.sprite.set_y_to

Sets the sprite's y-coordinate to a given value.

```python
stop.sprite.set_y_to(
  y
)

# EXAMPLE
sprite.set_y_to(100) # moves the sprite to y-coordinate 100
```
Required:
`x` - What to set the sprite's y-coordinate to

<br>

#### stop.sprite.if_on_edge_bounce

If the sprite is touching the edge of the window on the current frame, its direction will change so that if it were to 'move' in the current direction it would appear to have 'bounced' off of the edge.

```python
stop.sprite.if_on_edge_bounce()

# EXAMPLE
sprite.if_on_edge_bounce() # if the sprite is touching the edge of the screen it will point away from the edge
```

<br>

#### stop.sprite.set_rotation_style

Changes how the sprite visually looks when its direction is changed.

```python
stop.sprite.set_rotation_style(
  option
)

# EXAMPLE
sprite.set_rotation_style("all_around") # sets the sprite to rotate all around
sprite.set_rotation_style("dont_rotate") # sets the sprite to not rotate
sprite.set_rotation_style("left_right") # sets the sprite to flip left and right
```
Required:
`option` - Can be one of:
- `"all_around"` - The sprite visually can rotate in all directions.
- `"dont_rotate"` - The sprite doesn't visually rotate at all.
- `"left_right"` - The sprite visually flips left or right.

<br>

#### stop.sprite.say_for_seconds

Creates a speech bubble next to the sprite with some text, which disappears after a given amount of time.

```python
stop.sprite.say_for_seconds(
  speech,
  seconds
)

# EXAMPLE
sprite.say_for_seconds("hello world", 2) # a speech bubble says 'hello world' for 2 seconds
```
Required:
`speech` - The text in the speech bubble.
`seconds` - The duration of the speech bubble.

<br>

#### stop.sprite.say

Creates a speech bubble next to the sprite with some text.

```python
stop.sprite.say(
  speech,
  seconds
)

# EXAMPLE
sprite.say("hello world") # a speech bubble says 'hello world'
```
Required:
`speech` - The text in the speech bubble.

<br>

#### stop.sprite.think_for_seconds

Creates a thought bubble next to the sprite with some text, which disappears after a given amount of time.

```python
stop.sprite.think_for_seconds(
  thought,
  seconds
)

# EXAMPLE
sprite.think_for_seconds("hello world", 2) # a thought bubble says 'hello world' for 2 seconds
```
Required:
`thought` - The text in the thought bubble.
`seconds` - The duration of the thought bubble.

<br>

#### stop.sprite.think

Creates a thought bubble next to the sprite with some text.

```python
stop.sprite.think(
  thought
)

# EXAMPLE
sprite.think("hello world") # a thought bubble says 'hello world'
```
Required:
`thought` - The text in the thought bubble.

<br>

#### stop.sprite.switch_costume_to

Changes the image used to represent the sprite, to a given one.

```python
stop.sprite.switch_costume_to(
  costume
)

# EXAMPLE
sprite.switch_costume_to("apple1") # tries to switch to costume with name 'apple1'
sprite.switch_costume_to(4) # tries to switch costume to costume at index 4
```
Required:
`costume` - Can be one of:
- `[an integer]` - Switches to the costume with the index of the integer given. If integer is out of range of costume indexes, it loops around (using modulo).
- `[a string]` - Switches to the costume with the name of the string given. If no costume has that name, it tries to use the string as an index for a costume. If string is not an integer, the costume doesn't change.

<br>

#### stop.sprite.next_costume

Changes the sprite's current costume to the next index.

```python
stop.sprite.next_costume()

# EXAMPLE
sprite.next_costume() # switches to the next costume
```

<br>

#### stop.sprite.change_size_by

Changes the sprite's size percentage. This is what percent of the sprite's original size it should be displayed at.

```python
stop.sprite.change_size_by(
  percentage
)

# EXAMPLE
sprite.change_size_by(-20) # decreases the sprite's size by 20%
```
Required:
`percentage` - The amount to change the sprite's size by.

<br>

#### stop.sprite.set_size_to

Sets the sprite's size percentage to a given value. This is what percent of the sprite's original size it should be displayed at.

```python
stop.sprite.set_size_to(
  percentage
)

# EXAMPLE
sprite.set_size_to(50) # sets the sprite's size to 50%
```
Required:
`percentage` - The value to set the sprite's size.

<br>

#### stop.sprite.show

Makes the sprite visible (if previously invisible).

```python
stop.sprite.show()

# EXAMPLE
sprite.show() # makes the sprite visible
```

<br>

#### stop.sprite.hide

Makes the sprite invisible (if previously visible).

```python
stop.sprite.hide()

# EXAMPLE
sprite.hide() # makes the sprite invisible
```
