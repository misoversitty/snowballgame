import pygame
from Project.Entities.Player import Player
from Project.Services.Collision import Collision


class CollisionDetector:
    @staticmethod
    def isCollided(player: Player, group: pygame.sprite.Group):
        result = False
        collisionList = pygame.sprite.spritecollide(player, group, dokill=False, collided=pygame.sprite.collide_mask)
        if len(collisionList) > 1:
            result = []
            for count, collidedSprite in enumerate(collisionList):
                if count == 0:
                    continue
                result.append(Collision(player, collidedSprite))
        return result
