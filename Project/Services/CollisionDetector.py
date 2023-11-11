from pygame.sprite import Group, spritecollide
from Project.DataStructures.PlayerGroup import PlayerGroup
from Project.DataStructures.BulletGroup import BulletGroup
from Project.Entities.Player import Player
from Project.Services.Collision import Collision
from multipledispatch import dispatch


class CollisionDetector:
    @staticmethod
    @dispatch(Player, PlayerGroup)
    def getCollisions(player: Player, group: PlayerGroup):
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
    @dispatch(Player, BulletGroup)
    def getCollisions(player: Player, group: BulletGroup):
        result = False
        collisionList = spritecollide(player, group, dokill=False)
        if len(collisionList) > 0:
            result = True
        return result

    @staticmethod
    def filterCollisionList(index, ignorable=None):
        if index == ignorable:
            return False
        else:
            return True
