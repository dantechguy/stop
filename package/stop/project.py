from . import events

class Project:
    def __init__(self):
        self.green_flag_functions = []
        self.events = events.EventHandler(['green_flag'])

    def run(self):
        self.events.run('green_flag')
