import pygame
from Project.Entities.Player import Player

delta = 10

class Collision:
    def __init__(self, mainSprite: pygame.sprite, obj2: pygame.sprite):
        self.mainSprite = mainSprite
        self.obj2 = obj2
        self.blockedSidesOfMainSprite = self.guessSeveralSides()

    def guessSeveralSides(self):
        side = {
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False
        }
        croppedArea = self.mainSprite.rect.clip(self.obj2)
        if croppedArea.height >= delta:
            if croppedArea.centery < self.mainSprite.rect.centery:
                side["UP"] = True
            elif croppedArea.centery > self.mainSprite.rect.centery:
                side["DOWN"] = True
        if croppedArea.width >= delta:
            if croppedArea.centerx < self.mainSprite.rect.centerx:
                side["LEFT"] = True
            elif croppedArea.centerx > self.mainSprite.rect.centerx:
                side["RIGHT"] = True
        return side

    def getBlockedSides(self):
        res = []
        for key, value in self.blockedSidesOfMainSprite.items():
            if value:
                res.append(key)
        return res
