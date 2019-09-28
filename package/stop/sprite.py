from . import sprite_code
path = "{0}/../assets/".format(__file__) # replace with prefs file

class Sprite:
    def __init__(self, 
                    project, 
                    layer_order=1, 
                    visible=True, 
                    draggable=False,
                    rotation_style='all around',
                    costumes=[
                        {"file":"{0}costume1.png".format(path), "name":"costume1"}, 
                        {"file":"{0}costume2.png".format(path), "name":"costume2"}
                    ],
                    x=0,
                    y=0,
                    size=100,
                    direction=90,
                    costume_number=0,
                    volume=100
                ):
        self.project = project

        parameters = {
            'project': project,
            'canvas': project.canvas_object,
            'sprite_container': self,
            'layer_order': layer_order,
            'visible': visible,
            'draggable': draggable,
            'rotation_style': rotation_style,
            'costumes': costumes,

            'x': x,
            'y': y,
            'size': size,
            'direction': direction,
            'costume_number': costume_number,
            'volume': volume
        }

        self.sprite_code = sprite_code.SpriteCode(parameters)
        

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            function_name = name
            function_arguements = args
            self.add_instruction_to_queue(function_name, function_arguements)
        return wrapper

    def add_instruction_to_queue(self, block, parameters):
        item_function = getattr(self.sprite_code, block)
        item = {
            'function': item_function,
            'parameters': parameters
        }
        self.project.queue.put(item)