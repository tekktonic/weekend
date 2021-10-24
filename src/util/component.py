from enum import Enum

ComponentType = Enum('ComponentType', 'Stats Health Mana Equipment Spells Position Sprite Player Enemy')

class Component(object):
    def __init__(self, active=True):
        self.active = active

    def connect(self, id):
        pass
    
    def name(self):
        return type(self).__name__
    
    def get_type(self):
        return ComponentType[self.name()]

