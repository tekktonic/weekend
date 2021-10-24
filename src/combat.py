import sys

import pygame

import util.dice as dice
from util.component import ComponentType
from util.spritesheet import SpriteSheet
import util.resources as resources
from util.consts import FRAME
import util.scene as scene
import util.entity as entity

from systems.draw import DrawSystem

import components.player
import components.position
import components.sprite
import components.stats
import components.enemy
import components.stats
import components.health

class Scene(scene.Scene):
    def __init__(self, screen, stack):
        super().__init__(screen, stack, post_systems=[DrawSystem([ComponentType.Position, ComponentType.Sprite])])
        
        self.player = entity.Entity(self, set([
            components.player.Player(),
            components.position.Position(160, 100),
            components.sprite.Sprite('so', 16, 16, animations=[('idle', 0, 3, 0, 10 * FRAME)], animation='idle'),
            components.stats.Stats(dice.roll(1, 6), dice.roll(1, 6), dice.roll(1,6)),
            components.health.Health()]))

        self.enemy = entity.Entity(self, set([
            components.enemy.Enemy(),
            components.position.Position(130, 32),
            components.sprite.Sprite('ratking', 16, 16, animations=[('laugh', 0, 1, 0, 10 * FRAME)], animation='laugh'),
            components.stats.Stats(dice.roll(1, 3), dice.roll(1, 3), dice.roll(1,3)),
            components.health.Health()]))

        self.text = pygame.font.Font(resources.font_path("Bitmgothic"), 16).render('But I Want To Be The King', False, (0, 0, 0))
                
    def update(self, events, dt):
        self.screen.blit(self.text, (64, 64))
        self.system_manager.update(events, dt)
