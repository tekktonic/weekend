import enum

import pygame

import util.resources as resources

class SpriteSheet(object):
    def __init__(self, sheetname, tile_width, tile_height):
        path = resources.image_path(sheetname)
        print(path)
        self.backing_image = pygame.image.load(path)
        (w, h) = self.backing_image.get_size()
        # Make sure the image is evenly divisible by the tile size
        assert(w % tile_width == 0 and h % tile_height == 0)

        self.w = w
        self.h = h
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.names = {}
    
    def name(self, n, pos):
        self.names.set(n, pos)
    
    def get(self, v):
        if type(v) == type(tuple()):
            return self._get(v)
        elif issubclass(type(v), enum.Enum) or type(v) == type(''):
            return self._get(self.names.get(v))
        else:
            raise ValueError("Spritesheet key must be an (x,y) tuple, an enum value, or a string")

    def _get(self, v):
        (x, y) = v
        real_x = x * self.tile_width
        real_y = y * self.tile_width
        if (self.w < real_x + self.tile_width or self.h < real_y + self.tile_height
            or real_x < 0 or real_y < 0):
            raise ValueException("Tile out of bounds! Image is {} by {} but tried to pull a {} by {} tile out at {}, {}".format(self.w, self.h, self.tile_width, self.tile_height, real_x, real_y))
        return pygame.Rect(real_x, real_y, self.tile_width, self.tile_height)
