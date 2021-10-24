from util.system import System
from util.component import ComponentType

def DrawSystem(System):
    def __init__(self, screen, required_components):
        super().__init__(required_components)
        self.screen = screen
    def update(self, scene, entity):
        screen.blit(scene.components.get(ComponentType.Sprite)[entity.id].spritesheet.get(), scene.components.get(ComponentType.Position)[entity.id].pos)
