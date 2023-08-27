import pygame
from Project.Entities.Player import Player


class Collision:
    def __init__(self, mainSprite: pygame.sprite, obj2: pygame.sprite):
        self.mainSprite = mainSprite
        self.obj2 = obj2
        self.sideOfMainSprite = self.guessSide()

    def guessSide(self):
        side = ""
        croppedArea = self.mainSprite.rect.clip(self.obj2)
        if croppedArea.left < self.mainSprite.rect.centerx:
            side = "LEFT"
        if croppedArea.left > self.mainSprite.rect.centerx:
            side = "RIGHT"
        if croppedArea.top > self.mainSprite.rect.centery:
            side = "DOWN"
        if croppedArea.top < self.mainSprite.rect.centery:
            side = "UP"
        return side
