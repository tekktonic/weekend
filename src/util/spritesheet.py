import enum

import pygame

import util.resources as resources

class SpriteSheet(object):
    class Animation(object):
        def __init__(self, start_x, end_x, y, frame_timing):
            self.start_x = start_x
            self.end_x = end_x
            self.y = y
            self.frame_timing = frame_timing
            self.frame_clock = frame_timing
    
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
        self.animations = {}
        self.current_animation = None
        self.frame = 0
    
    def animation(self, name, start_x, end_x, y, timing):
        self.animations[name] = self.Animation(start_x, end_x, y, timing)
        self.frame = start_x
    
    def set_animation(self, name):
        self.current_animation = name
        
    def next(self, dt):
        anim = self.animations[self.current_animation]
        anim.frame_clock -= dt
        if anim.frame_clock <= 0:
            self.frame += 1
            if self.frame > self.animations[self.current_animation].end_x:
                self.frame = self.animations[self.current_animation].start_x
            anim.frame_clock = anim.frame_timing
    
    def get(self, dt):
        self.next(dt)
        ret = pygame.Surface((self.tile_width, self.tile_height), flags=pygame.SRCALPHA)
        ret.blit(self.backing_image, (0, 0), self._get((self.frame, self.animations[self.current_animation].y)))
        return ret
    
    def set(self, v):
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
