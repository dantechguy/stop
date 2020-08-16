class Sprite:
    def __init__(self, project, *args, **kwargs):
        self.project = project
        project.events.subscribe_tagged_methods(self)
        self.setup(*args, **kwargs)
        
    def setup(self, *args, **kwargs):
        pass

    def move(self, steps):
        print('move', steps)

    def turn(self, degrees):
        print('turn', degrees)
