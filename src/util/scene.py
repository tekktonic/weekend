
from util.system import SystemManager

class SceneStack(object):
    def __init__(self, initial_scene):
        self.scenes = [initial_scene]
   
    def current(self):
        return self.scenes[len(self.scenes) - 1]
        
    def replace(self, scene):
        self.scenes[len(self.scenes) - 1] = scene
        
    def push(self, scene):
        self.scenes.append(scene)
    
    def pop(self):
        self.scenes.pop()

    def clear(self):
        self.scenes = []

    def running(self):
        return len(self.scenes) > 0
 
class Scene(object):
    def __init__(self, screen, stack, *args):
        self.system_manager = SystemManager(args)
        self.screen = screen
        self.stack = stack
            
    def update(self, events, dt):
        pass    
