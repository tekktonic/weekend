
from util.system import SystemManager

from util.entity import ComponentType
_max_entities = 255

class SceneStack(object):
    def __init__(self):
        self.scenes = []
    
    def current(self):
        return self.scenes[len(self.scenes) - 1]
       
    def get(self, back):
        return self.scenes[len(self.scenes - back - 1)]
     
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
    def __init__(self, screen, stack, systems=[], post_systems=[]):
        self.system_manager = SystemManager(self, systems, post_systems)
        self.screen = screen
        self.stack = stack
        self.components = {}
        for t in ComponentType:
            self.components[t] = [None for x in range(_max_entities)]
        self.entities = [None for _ in range(_max_entities)]
        
    def find_next_id(self):
        for i in range(_max_entities):
            if self.entities[i] == None:
                return i
        raise IndexError("More than 255 entities used")

    def update(self, events, dt):
        pass    
