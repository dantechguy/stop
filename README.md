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
- [Project Class](#project-class)
- [Sprite Class](#sprite-class)
- [Scratch Maths](#scratch-maths)

## Project Class

### Create a project object:

```python
project = stop.Project(
  fps=60  # optional, specifies custom project fps
)
```





## Sprite Class

```python
sprite = stop.Sprite(project, )
```