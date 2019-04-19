import threading

class Stage:
    def __init__(self):
        self.isStage
        self.name
        self.variables
        self.lists
        self.broadcasts
        self.blocks
        self.comments
        self.currentCostume
        self.costumes
        self.sounds
        self.volume
        self.layerOrder
        self.tempo
        self.videoTransparency
        self.videoState
        self.textToSpeechLanguage

class Sprite:
    def __init__(self):
        self.canvas = 
        #
        self.id = 
        self.isStage
        self.name
        self.variables
        self.lists
        self.broadcasts
        self.blocks
        self.comments
        self.currentCostume
        self.costumes
        self.sounds
        self.volume
        self.layerOrder
        self.visible
        self.x
        self.y
        self.size
        self.direction
        self.draggable
        self.rotationStyle

    def turn_right(self, degrees):
        pass

class Block:
    def __init__(self):
        pass

    def convert(self):
        # returns a python code equivalent
        pass


# gives us the list of all blocks from one sprite. 
# each sprite has one main list which contains other lists of blocks
# add a list with the block in it to a main list whenever we find a top level block

# create a block class, which has a "python equlivant function"
# if it requires extra blocks, include their block classes as attributes

# should you run each script as a separate thread?

# using file writing create other python files. import them when running game
# each file is a separate script, or maybe a separate sprite

# the sprite class has methods that relate to scratch blocks