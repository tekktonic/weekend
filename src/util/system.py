
class System(object):
    def __init__(self, required_components):
        self.required_components = required_components
        
    def update(self, events, scene, entity, dt):
        print("You forgot to actually implement your system")

class SystemManager(object):
    def __init__(self, scene, systems=[], post_systems=[]):
        self.scene = scene
        self.systems = systems
        self.post_systems = systems

    def update(self, events, dt):
        for system in self.systems:
            for entity in self.scene.entities:
                if system.requires.issubset(entity.components_used):
                    system.update(scene, entity, dt)
        for system in self.post_systems:
            for entity in self.scene.entities:
                if system.requires.issubset(entity.components_used):
                    system.update(events, scene, entity, dt)
