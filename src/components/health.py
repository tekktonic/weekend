from ..util.entity import ComponentType, Component

class Health(Component):
    def __init__(self, max):
        super().__init__()
        self.hp = max
