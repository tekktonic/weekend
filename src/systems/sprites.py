from util.system import System
from util.component import ComponentType

class Sprites(System):
    def __init__(self, screen):
        super().__init__({ ComponentType.Position, ComponentType.Sprite})
        self.screen = screen
    
    def update(self, events, scene, entity, dt):
        self.screen.blit(scene.components.get(ComponentType.Sprite)[entity.id].spritesheet.get(dt), scene.components.get(ComponentType.Position)[entity.id].pos)
