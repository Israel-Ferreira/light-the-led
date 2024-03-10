import inspect


def load_instance_config():
    if not hasattr(inspect, 'getargspec'):
        inspect.getargspec =  inspect.getfullargspec

        