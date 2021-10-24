import sys

import pygame

from util.spritesheet import SpriteSheet
import util.resources as resources

from util.consts import FRAME

class Module():
    def __init__(self, screen):
        self.screen = screen
        self.sprite = SpriteSheet('so', 16, 16)
        print(self.sprite)
        self.sprite.animation('dance', 0, 3, 0, 10 * FRAME)
        self.sprite.set_animation('dance')
        
        self.ratking = SpriteSheet('ratking', 48, 64)
        self.ratking.animation('laugh', 0, 1, 0, 30 * FRAME)
        self.ratking.set_animation('laugh')
        self.frame = 0
        self.text = pygame.font.Font(resources.font_path("Bitmgothic"), 16).render('But I Want To Be The King', False, (0, 0, 0))
        self.anim_time = 20
                
    def step(self, events, dt):
        self.anim_time -= dt
        if self.anim_time <= 0:
            self.frame = (self.frame + 1) % 4
            self.anim_time = 20
        self.screen.blit(self.text, (64, 64))
        self.screen.blit(self.sprite.get(dt), (160, 100))
        self.screen.blit(self.ratking.get(dt), (140, 0))

        return True
