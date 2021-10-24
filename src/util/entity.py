from util.component import Component, ComponentType

class Entity(object):

    # Initial_components should be a list of objects. We'll use type to look up the array to put it in.
    def __init__(self, scene, initial_components: Component):
        self.scene = scene
        self.id = scene.find_next_id()
        scene.entities[self.id] = self
        self.used_components = set()
        for component in initial_components:
            print("CCCCCC: " + str(component.get_type()) + '    ' + str(type(component).__name__))
            print(self.id)
            self.scene.components.get(component.get_type())[self.id] =  component
            self.used_components.add(component.get_type())

        for component in self.used_components:
            self.scene.components.get(component)[self.id].connect(self)

    def add(self, c: Component):
        self.scene.components[c.type].insert(self.id, c)
        self.scene.components.get(component.get_type())[self.id].connect(self)

    def deactivate(self, c: ComponentType):
        self.scene.components[c][self.id].active = False
        self.used_components.remove(c)

    def remove(self, c: ComponentType):
        components[c][self.id] = Component(alive=False)
        self.used_components.remove(c)
    
    def __del__(self):
        for k,v in self.scene.components.items():
            if k in self.used_components:
                v[self.id].active = False
        self.scene.entities[self.id] = None
