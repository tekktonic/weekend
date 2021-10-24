import sys
from util.spritesheet import SpriteSheet

class Module():
    def __init__(self, screen):
        self.screen = screen
        self.sprite = SpriteSheet("so", 16, 16)
        self.count = 1000
        self.frame = 0
    
    def step(self, events, dt):
        self.count -= 1
        if (self.count % 10 == 1):
            self.frame = (self.frame + 1) % 4
        self.screen.blit(self.sprite.backing_image, (160, 100), self.sprite.get((self.frame + 3, 0)))
        return self.count > 0
