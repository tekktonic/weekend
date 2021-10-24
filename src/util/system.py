
class System(object):
    def __init__(self, required_components):
        self.required_components = required_components
        
    def update(self, events, scene, entity, dt):
        print("You forgot to actually implement your system")

class SystemManager(object):
    def __init__(self, scene, systems=[], post_systems=[]):
        print(post_systems)
        self.scene = scene
        self.systems = systems
        self.post_systems = post_systems

    def update(self, events, dt):
        for system in self.systems:
            for entity in self.scene.entities:
                if entity != None and system.required_components.issubset(entity.used_components):
                    system.update(events, self.scene, entity, dt)
        for system in self.post_systems:
            for entity in self.scene.entities:
                if entity != None and system.required_components.issubset(entity.used_components):
                    system.update(events, self.scene, entity, dt)
