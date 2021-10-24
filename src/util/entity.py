from enum import Enum

_max_entities = 255
_entity_slots = [False for x in range(_max_entities)]

def _find_next_id(list):
    for i in range(_max_entities):
        if _entity_slots[i]:
            _entity_slots[i] = True
            return i
    raise IndexError("More than 255 entities used")

# Keyed on a ComponentType
components = {}

ComponentType = Enum('ComponentType', 'Stats', 'Health', 'Mana', 'Equipment', 'Spells')

class Component(object):
    def __init__(self, active=True):
        self.active = active

    def connect(self, id):
        pass
        
    def get_type(self):
        ComponentType[type(self).__name__]

class Entity(object):
    # Initial_components should be a list of objects. We'll use type to look up the array to put it in.
    def __init__(self, initial_components: Component):
        self.id = _find_next_id(_entity_slots)
        self.used_components = set()
        for component in initial_components:
            components.get(component.get_type())[self.id] = component
            self.used_components.add(component.get_type())

        for component in self.used_components:
            components.get(component)[self.id].connect(self.id)

    def add(self, c: Component):
        components[c.type][self.id] = c

    def deactivate(self, c: ComponentType)
        components[c][self.id].active = False
        self.used_components.remove(c)

    def remove(self, c: ComponentType):
        components[c][self.id] = Component(alive=False)
        self.used_components.remove(c)
    
    def __del__(self):
        for c in components.iteritems()
            c[self.id].active = False
        _entity_slots[self.id] = False
