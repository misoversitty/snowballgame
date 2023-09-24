from pygame.sprite import Group, spritecollide
from Project.Entities.Player import Player
from Project.Services.Collision import Collision


class CollisionDetector:
    @staticmethod
    def getCollisions(player: Player, group: Group):
        result = False
        collisionList = spritecollide(player, group, dokill=False)
        if len(collisionList) > 1:
            filteredCollisionList = filter(lambda args:
                                           CollisionDetector.filterCollisionList(args[0], ignorable=player.No),
                                           enumerate(collisionList))
            filteredCollisionList = map(lambda args:
                                        args[1],
                                        filteredCollisionList)
            result = list(map(lambda collidedSprite:
                              Collision(player, collidedSprite),
                              filteredCollisionList))
        return result

    @staticmethod
    def filterCollisionList(index, ignorable=None):
        if index == ignorable:
            return False
        else:
            return True
