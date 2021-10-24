import sys

import pygame

from util.spritesheet import SpriteSheet
import util.resources as resources

class Module():
    def __init__(self, screen):
        self.screen = screen
        self.sprite = SpriteSheet("so", 16, 16)
        self.ratking = SpriteSheet('ratking', 48, 64)
        self.frame = 0
        self.text = pygame.font.Font(resources.font_path("Bitmgothic"), 16).render('But I Want To Be The King', False, (0, 0, 0))
        self.anim_time = 20
                
    def step(self, events, dt):
        self.anim_time -= dt
        if self.anim_time <= 0:
            self.frame = (self.frame + 1) % 4
            self.anim_time = 20
        self.screen.blit(self.text, (64, 64))
        self.screen.blit(self.sprite.backing_image, (160, 100), self.sprite.get((self.frame, 0)))
        self.screen.blit(self.ratking.backing_image, (140, 0), self.ratking.get((self.frame // 2, 0)))

        return True
