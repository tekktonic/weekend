from entity import components
class SystemManager(object):
    def __init__(self):
        self.systems = []

    def update(self, entities, dt):
        for system in systems:
            for entity in entities:
                if (system.requires.issubset(entity.components_used)):
                    system.update(entity, components, dt)
