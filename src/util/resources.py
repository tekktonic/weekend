import os

def _create_path(suffix):
    return os.path.dirname(os.path.realpath(__file__)) + '/../../resources/' + suffix + '/'

def image_path(filename):
    return _create_path("images") + filename + ".png"

def sound_path(filename):
    return _create_path("sounds") + filename + ".ogg"

def object_path(filename):
    return _create_path("objects") + filename + ".json"
