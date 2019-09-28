from . import canvas_object
import queue
import threading
import time



class Project:
    def __init__(self, fps=60):
        self.sprites = {}
        self.canvas_object = canvas_object.CanvasObject()
        self.queue = queue.Queue()
        self.fps = fps
        self.frame_time_ms = int(1000/fps)
        self.frame_time = 1/fps

        # event lists
        self.green_flag_events = {'all':[]}
        self.key_pressed_events = {}
        self.sprite_clicked_events = {}
        self.backdrop_switches_to_events = {}
        self.loudness_more_than_events = {}
        self.timer_more_than_events = {}
        self.receive_broadcast_events = {}

    def run(self):
        self.canvas_object.root.after(self.frame_time_ms, self.frame)
        self.send_green_flag_event()
        self.canvas_object.root.mainloop()

    def stop(self):
        self.canvas_object.root.destroy()

    def frame(self):
        for _ in range(self.queue.qsize()):
            item = self.queue.get()
            item_function = item['function']
            item_parameters = item['parameters']
            item_function(item_parameters)
            self.queue.task_done()

        self.canvas_object.root.after(self.frame_time_ms, self.frame)


    # BLOCKS

    def wait(self, seconds=False):
        if not seconds:
            seconds = self.frame_time
        time.sleep(seconds)

    def switch_backdrop_to(self, parameters): # backdrop name / number
        pass

    def next_backdrop(self, parameters):
        pass

    def stop_all_sounds(self, parameters):
        pass

    def create_clone_of(self, parameters): #sprite
        pass



    # ADD EVENTS

    def green_flag(self, function):
        self.add_event('all', function, self.green_flag_events)

    def key_pressed(self, key, function):
        self.add_event(key, function, self.key_pressed_events)

    def sprite_clicked(self, sprite, function):
        self.add_event(sprite, function, self.sprite_clicked_events)

    def backdrop_switches_to(self, backdrop_name, function):
        pass

    def loudness_more_than(self, loudness, function):
        pass

    def timer_more_than(self, timer, function):
        pass

    def receive_broadcast(self, message, function):
        self.add_event(message, function, self.receive_broadcast_events)

    def add_event(self, key, function, events_list):
        if key not in events_list:
            events_list[key] = []
        events_list[key].append(function)

    # SEND EVENTS

    def send_green_flag_event(self):
        self.send_event('all', self.green_flag_events)

    def send_sprite_clicked_event(self, sprite):
        self.send_event(sprite, self.sprite_clicked_events)

    def send_backdrop_switches_to_event(self, backdrop_name):
        self.send_event(backdrop_name, self.backdrop_switches_to_events)

    def send_loudness_more_than_event(self, loudness):
        self.send_event(loudness, self.loudness_more_than_events)

    def send_timer_more_than_event(self, timer):
        self.send_event(timer, self.timer_more_than_events)

    def send_receive_broadcast_event(self, message):
        self.send_event(message, self.receive_broadcast_events)

    def send_event(self, key, events_list):
        if key in events_list:
            specific_events_list = events_list[key]

            threads = []
            for method in specific_events_list:
                temp_thread = threading.Thread(target=method, daemon=True)
                threads.append(temp_thread)

            for thread in threads:
                thread.start()