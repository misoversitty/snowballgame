from pygame import Surface
from pygame.sprite import Sprite
from Project.DataStructures.Block import Block


class Obstacle(Sprite):
    def __init__(self, *args, block: Block):
        super().__init__(*args)
        self.image = Surface(block.getSize())
        self.image.fill([125, 127, 125])
        self.rect = self.image.get_rect()
        self.rect.topleft = block.getTopLeft()
