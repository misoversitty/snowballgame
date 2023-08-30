import pygame
from Project.Entities.Player import Player

delta = [2, 5]

class Collision:
    def __init__(self, mainSprite: pygame.sprite, obstacle: pygame.sprite):
        self.mainSprite = mainSprite
        self.obstacle = obstacle
        self.blockedSidesOfMainSprite = self.guessSeveralSides()

    def guessSeveralSides(self):
        side = {
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False
        }
        print(f"    self: top={self.mainSprite.rect.top}, bottom={self.mainSprite.rect.bottom}")
        print(f"obstacle: top={self.obstacle.rect.top}, bottom={self.obstacle.rect.bottom}")
        croppedArea = self.mainSprite.rect.clip(self.obstacle.rect)
        if croppedArea.width >= delta[0]:
            pass
        if self.mainSprite.rect.top < self.obstacle.rect.bottom and self.mainSprite.rect.centery > self.obstacle.rect.centery:
            side["UP"] = True
        elif self.mainSprite.rect.bottom > self.obstacle.rect.top and self.mainSprite.rect.centery < self.obstacle.rect.centery:
            side["DOWN"] = True
        if self.mainSprite.rect.left < self.obstacle.rect.right and self.mainSprite.rect.centerx > self.obstacle.rect.centerx:
            side["LEFT"] = True
        elif self.mainSprite.rect.right > self.obstacle.rect.left and self.mainSprite.rect.centerx < self.obstacle.rect.centerx:
            side["RIGHT"] = True
        return side

    def getBlockedSides(self):
        res = list(map(lambda item: item[0] if item[1] else None, self.blockedSidesOfMainSprite.items()))
        return res
