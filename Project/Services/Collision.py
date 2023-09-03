import pygame
from Project.Entities.Player import Player

delta = [7, 5]

class Collision:
    def __init__(self, mainSprite: pygame.sprite, obstacle: pygame.sprite):
        self.mainObject = mainSprite
        self.obstacle = obstacle
        self.blockedSides = self.guessSeveralSides()

    def guessSeveralSides(self):
        side = set()
        croppedArea = self.mainObject.rect.clip(self.obstacle.rect)
        if delta[0] <= croppedArea.width < croppedArea.height:
            if self.mainObject.rect.centerx > croppedArea.centerx:
                side.add("LEFT")
            elif self.mainObject.rect.centerx < croppedArea.centerx:
                side.add("RIGHT")
        elif delta[0] <= croppedArea.height < croppedArea.width:
            if self.mainObject.rect.centery > croppedArea.centery:
                side.add("UP")
            elif self.mainObject.rect.centery < croppedArea.centery:
                side.add("DOWN")

        return side
