from util.system import System
from util.component import ComponentType
import pygame
import util.resources as resources

class DrawHP(System):
    def __init__(self, screen):
        super().__init__({ ComponentType.Position, ComponentType.Health})
        self.screen = screen
        self.font = pygame.font.Font(resources.font_path("tiny"), 6)
    
    def update(self, events, scene, entity, dt):
        (x, y) = scene.components.get(ComponentType.Position)[entity.id].pos
        hp = scene.components.get(ComponentType.Health)[entity.id].hp
        self.screen.blit(self.font.render("HP: {}".format(hp), False, (0, 0, 0)), (x, y - 8))
