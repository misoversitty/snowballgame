import pygame
from Project.Services.ImageLoader import ImageLoader


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = ImageLoader.LoadImage('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        pass
