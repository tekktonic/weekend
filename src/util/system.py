
class System(object):
    def __init__(self, required_components):
        self.required_components = required_components
        
    def update(self, entity, required_components):
        print("You forgot to actually implement your system")

class SystemManager(object):
    def __init__(self, scene, systems=[], post_systems=[]):
        self.scene = scene
        self.systems = systems
        self.post_systems = systems

    def update(self, entities, dt):
        for system in self.systems:
            for entity in self.scene.entities:
                if system.requires.issubset(entity.components_used):
                    system.update(entity, dt)
        for system in self.post_systems:
            for entity in self.scene.entities:
                if system.requires.issubset(entity.components_used):
                    system.update(entity, dt)
