
class System(object):
    def __init__(self, required_components):
        self.required_components = required_components
        
    def update(self, entity, required_components):
        print("You forgot to actually implement your system")

class SystemManager(object):
    def __init__(self, *args):
        self.systems = []
        for arg in args:
            self.systems.append(arg)

    def update(self, entities, dt):
        for system in systems:
            for entity in entities:
                if system.requires.issubset(entity.components_used):
                    system.update(entity, dt)
