from util.component import Component

from util.spritesheet import SpriteSheet

class Sprite(Component):
    def __init__(self, file, tile_w, tile_h, animations, animation):
        self.spritesheet = SpriteSheet(file, tile_w, tile_h)
        for a in animations:
            (name, xs, xe, y, t) = a
            self.spritesheet.animation(name, xs, xe, y, t)
        self.spritesheet.set_animation(animation)
