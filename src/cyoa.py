import sys

count = 1000
def step(events, dt):
    module = sys.modules[__name__]
    module.count -= 1
    return module.count > 0
