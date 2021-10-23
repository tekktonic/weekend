from ..util.entity import ComponentType, Component

class Mana(Component):
    def __init__(self, max):
        super().__init__()
        self.mp = max
