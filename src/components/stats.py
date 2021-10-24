from util.entity import Component

class Stats(Component):
    def __init__(self, s, i, d):
        super().__init__()
        self.strength = s
        self.intelligence = i
        self.dexterity = d
