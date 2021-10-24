from util.entity import Component
from enum import Enum

ActionType = Enum("ActionType", "Attack", "Use", "Magic")

class Action(Component):
    def __init__(self, sel_action, target, data=None):
        super().__init__()
        self.sel_action = sel_action
        self.data = data
        self.target = target