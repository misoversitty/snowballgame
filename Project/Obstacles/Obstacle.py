from pygame import Surface
from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.image = Surface((kwargs.get("rect")[][]))
        self.rect = self.image.get_rect()
        self.rect.topleft = kwargs.get("rect")