# S.To.P (Scratch To Python)

See the full documentation at this repository's [wiki](https://github.com/dantechguy/stop/wiki).

## Overview

This is a library designed for two purposes:

1. Converting Scratch projects into Python code
2. Being able to use Python in similar ways to Scratch


## Quick Start Guide

```python
# imports all the code from the S.To.P library
import stop

# creates a new project. each new 'project' creates a new window
# each 'project' represents a scratch project, each which contains sprites
project = stop.Project()

# creates a new sprite for the project that was just made
# pass the project it belongs to, and a dictionary of custom parameters
sprite1 = stop.Sprite(project, {})

# define a function, controlling the sprite
def run_around_in_circles():
    while True:
        sprite1.move_steps(10)
        sprite1.turn_degrees(15)
        # makes the screen update every loop
        project.wait()

# adds the function to a list, which are all run when the project runs
project.add_green_flag_event(run_around_in_circles)

# runs the project
project.run()
```