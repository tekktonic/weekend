import sys

import pygame

from util.spritesheet import SpriteSheet
import util.resources as resources


class Module():
    def __init__(self, screen):
        self.screen = screen
        self.sprite = SpriteSheet("so", 16, 16)
        self.frame = 0
        self.passive = pygame.Color(0, 0, 0, )
        self.active = pygame.Color(255, 255, 255)
        self.borderWidth = 2

        self.fightText = pygame.font.Font(resources.font_path("prstart"), 8).render('Attack', False, (0, 0, 0))
        self.magicText = pygame.font.Font(resources.font_path("prstart"), 8).render('Magic', False, (0, 0, 0))
        self.infoText = pygame.font.Font(resources.font_path("prstart"), 8).render('Info', False, (0, 0, 0))
        # self.fightButton = pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), self.fightRect)
        # self.magicButton = pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), self.fightRect)
        # self.infoButton = pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), self.fightRect)
        self.fr = pygame.Rect(15, 175, 55, 15 + self.borderWidth)
        self.mr = pygame.Rect(115, 175, 45, 15 + self.borderWidth)
        self.ir = pygame.Rect(215, 175, 40, 15 + self.borderWidth)

        self.anim_time = 20

    def step(self, events, dt):
        self.anim_time -= dt
        if self.anim_time <= 0:
            self.frame = (self.frame + 1) % 4
            self.anim_time = 20

        mousepos = pygame.mouse.get_pos()
        self.screen.blit(self.fightText, (20, 180))
        if self.fr.collidepoint(mousepos):
            # If our mouse is hovering over the box; check for click logic here too
            draw_borders(self.screen, self.fr.x, self.fr.y, self.fr.width, self.fr.height, self.borderWidth,
                         self.active)
        else:
            draw_borders(self.screen, self.fr.x, self.fr.y, self.fr.width, self.fr.height, self.borderWidth,
                         self.passive)

        self.screen.blit(self.magicText, (120, 180))
        if self.mr.collidepoint(mousepos):
            draw_borders(self.screen, self.mr.x, self.mr.y, self.mr.width, self.mr.height, self.borderWidth,
                         self.active)
        else:
            draw_borders(self.screen, self.mr.x, self.mr.y, self.mr.width, self.mr.height, self.borderWidth,
                         self.passive)

        self.screen.blit(self.infoText, (220, 180))
        if self.ir.collidepoint(mousepos):
            draw_borders(self.screen, self.ir.x, self.ir.y, self.ir.width, self.ir.height, self.borderWidth,
                         self.active)
            # pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), self.ir)
        else:
            draw_borders(self.screen, self.ir.x, self.ir.y, self.ir.width, self.ir.height,
                         self.borderWidth, self.passive)
            # pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), self.ir)

        self.screen.blit(self.sprite.backing_image, (160, 100), self.sprite.get((self.frame, 0)))
        return True


def draw_borders(s, x, y, w, h, bw, c):
    pygame.draw.line(s, c, (x - bw // 2 + 1, y), (x + w + bw // 2, y), bw)
    pygame.draw.line(s, c, (x - bw // 2 + 1, y + h), (x + w + bw // 2, y + h), bw)
    pygame.draw.line(s, c, (x, y - bw // 2 + 1), (x, y + h + bw // 2), bw)
    pygame.draw.line(s, c, (x + w, y - bw // 2 + 1), (x + w, y + h + bw // 2), bw)
