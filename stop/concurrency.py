from kivy.clock import Clock
import threading


def run_in_thread(func):
    def decorator(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        t.start()
        return t

    return decorator
