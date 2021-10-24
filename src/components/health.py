from util.entity import Component, ComponentType

class Health(Component):
    def __init__(self, max=None):
        super().__init__()
        self.hp = max
    
    def connect(self, e):
        if self.hp == None:
            self.hp = e.scene.components.get(ComponentType.Stats)[e.id].strength * 10
