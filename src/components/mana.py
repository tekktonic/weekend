from util.entity import Component

class Mana(Component):
    def __init__(self, max):
        super().__init__()
        self.mp = max
