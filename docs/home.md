### Introduction to the `project` object

The `project` object is the first thing you make when creating a S.To.P project. It is the central 'hub' for everything related to the current project, including executing code and storing information.

## Methods

### Create a `project`

```python
import stop
project = stop.Project()
```
**Arguments:**
- (optional) `fps = 30`
  - Decides the frame rate of the project

<br>

### `project.run()`

**Description:**
This creates the project window and starts to execute your code. Without this, nothing will happen. After the window has been closed, any code afterwards will then be run.

```python
import stop

project = stop.Project()

# your code here

project.run()
```

<br>

### `project.stop()`

**Description:**
Stops the entire project from running, and closes the window. All code after `project.run()` will then be executed.

```python
import stop

project = stop.Project()

def stop_after_one_second():
    project.wait(1)
    project.stop()

project.run()
```

<br>

### `project.wait()`