import sys

import pygame

import util.dice as dice
from util.component import ComponentType
from util.spritesheet import SpriteSheet
import util.resources as resources
from util.consts import FRAME
import util.scene as scene
import util.entity as entity

from systems.draw import Draw

import components.player
import components.position
import components.sprite
import components.stats
import components.enemy
import components.stats
import components.health


class Scene(scene.Scene):

    def __init__(self, screen, stack):
        super().__init__(screen, stack, post_systems=[Draw(screen)])
        
        self.passive = pygame.Color(0, 0, 0, )
        self.active = pygame.Color(255, 255, 255)
        self.main_button_width = 2
        self.fightText = pygame.font.Font(resources.font_path("prstart"), 8).render('Attack', False, (0, 0, 0))
        self.magicText = pygame.font.Font(resources.font_path("prstart"), 8).render('Magic', False, (0, 0, 0))
        self.infoText = pygame.font.Font(resources.font_path("prstart"), 8).render('Info', False, (0, 0, 0))
        self.fr = pygame.Rect(15, 175, 55, 15 + self.main_button_width)
        self.mr = pygame.Rect(115, 175, 45, 15 + self.main_button_width)
        self.ir = pygame.Rect(215, 175, 40, 15 + self.main_button_width)
        self.mouseResolved = False
        self.optionSelected = ""

        self.spell_border = 1
        self.spell_height = 10
        self.spell_width = 90
        # Name, Mana cost
        self.spells = [["Fire bolt", 1], ["Water Bomb", 2], ["Dark Spear", 4], ["Fireball", 6]]
        # Text, Rectangle
        self.spell_rects = []
        for i, s in enumerate(self.spells):
            self.spell_rects.append([
                pygame.font.Font(resources.font_path("tiny"), 6).render(s[0] + " (" + str(s[1]) + ")", False,(0, 0, 0)),
                pygame.Rect(self.mr.x + 10, self.mr.y - self.spell_height*(i+1) - 1, self.spell_width, self.spell_height)
            ])

        self.player = entity.Entity(self, set([
            components.player.Player(),
            components.position.Position(160, 100),
            components.sprite.Sprite('so', 16, 16, animations=[('idle', 0, 3, 0, 10 * FRAME)], animation='idle'),
            components.stats.Stats(dice.roll(1, 6), dice.roll(1, 6), dice.roll(1, 6)),
            components.health.Health()]))

        self.enemy = entity.Entity(self, set([
            components.enemy.Enemy(),
            components.position.Position(130, 32),
            components.sprite.Sprite('ratking', 48, 64, animations=[('laugh', 0, 1, 0, 10 * FRAME)], animation='laugh'),
            components.stats.Stats(dice.roll(1, 3), dice.roll(1, 3), dice.roll(1,3)),
            components.health.Health()]))

        self.text = pygame.font.Font(resources.font_path("Bitmgothic"), 16).render('But I Want To Be The King', False,
                                                                                   (0, 0, 0))

    def update(self, events, dt):
        self.screen.blit(self.text, (64, 64))
        self.system_manager.update(events, dt)
        self.handle_buttons()

    def handle_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0]
        self.screen.blit(self.fightText, (20, 180))
        self.screen.blit(self.magicText, (120, 180))
        self.screen.blit(self.infoText, (220, 180))
        if self.optionSelected == "Magic":
            for i, s in enumerate(self.spell_rects):
                self.screen.blit(s[0], (s[1].x+5, s[1].y+2))
                if s[1].collidepoint(mouse_pos):
                    self.draw_borders(self.screen, s[1].x, s[1].y, s[1].width, s[1].height-self.spell_border,
                                      self.spell_border, self.active)
                    if pressed:
                        print("Casting: " + self.spells[i][0])
                else:
                    self.draw_borders(self.screen, s[1].x, s[1].y, s[1].width, s[1].height - self.spell_border,
                                      self.spell_border, self.passive)

        if not pressed and self.mouseResolved:
            self.mouseResolved = False

        if self.fr.collidepoint(mouse_pos):
            # If our mouse is hovering over the box; check for click logic here too
            self.draw_borders(self.screen, self.fr.x, self.fr.y, self.fr.width, self.fr.height - self.main_button_width,
                              self.main_button_width, self.active)
            if pressed:
                self.handle_click("Attack")

        else:
            self.draw_borders(self.screen, self.fr.x, self.fr.y, self.fr.width, self.fr.height - self.main_button_width,
                              self.main_button_width, self.passive)

        if self.mr.collidepoint(mouse_pos):
            self.draw_borders(self.screen, self.mr.x, self.mr.y, self.mr.width, self.mr.height - self.main_button_width,
                              self.main_button_width, self.active)
            if pressed:
                self.handle_click("Magic")
        else:
            self.draw_borders(self.screen, self.mr.x, self.mr.y, self.mr.width, self.mr.height - self.main_button_width,
                              self.main_button_width, self.passive)

        if self.ir.collidepoint(mouse_pos):
            self.draw_borders(self.screen, self.ir.x, self.ir.y, self.ir.width, self.ir.height - self.main_button_width,
                              self.main_button_width, self.active)
            if pressed:
                self.handle_click("Info")
        else:
            self.draw_borders(self.screen, self.ir.x, self.ir.y, self.ir.width, self.ir.height - self.main_button_width,
                              self.main_button_width, self.passive)

        if pressed:
            if not self.mouseResolved:
                self.mouseResolved = True
                self.optionSelected = ""

    def handle_click(self, button_name):
        if not self.mouseResolved:
            # do logic for actions here
            print(button_name + " pressed")
            self.mouseResolved = True
            self.optionSelected = button_name

    def draw_borders(self, s, x, y, w, h, bw, c):
        pygame.draw.line(s, c, (x - bw // 2 + 1, y), (x + w + bw // 2, y), bw)
        pygame.draw.line(s, c, (x - bw // 2 + 1, y + h), (x + w + bw // 2, y + h), bw)
        pygame.draw.line(s, c, (x, y - bw // 2 + 1), (x, y + h + bw // 2), bw)
        pygame.draw.line(s, c, (x + w, y - bw // 2 + 1), (x + w, y + h + bw // 2), bw)
