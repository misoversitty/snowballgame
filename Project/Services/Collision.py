import pygame
from Project.Entities.Player import Player


class Collision:
    def __init__(self, mainSprite: pygame.sprite, obj2: pygame.sprite):
        self.mainSprite = mainSprite
        self.obj2 = obj2
        self.collisionPointOfMainSprite = pygame.sprite.collide_mask(mainSprite, obj2)
        self.sideOfMainSprite = self.guessSide()

    def guessSide(self):
        #self.mainSprite.rect.height
        #self.mainSprite.rect.width
        if self.collisionPointOfMainSprite[0] and self.collisionPointOfMainSprite[1] < 10:
            print('BLOCK_UP')
        if self.collisionPointOfMainSprite[0] and self.collisionPointOfMainSprite[1] > 20:
            print('BLOCK_DOWN')
        if self.collisionPointOfMainSprite[0] < 10 and self.collisionPointOfMainSprite[1]:
            print('BLOCK_LEFT')
        if self.collisionPointOfMainSprite[0] > 20 and self.collisionPointOfMainSprite[1]:
            print('BLOCK_RIGHT')
        return 0
