from pygame.sprite import Group, spritecollide
from Project.DataStructures.PlayerGroup import PlayerGroup
from Project.DataStructures.BulletGroup import BulletGroup
from Project.DataStructures.ObstacleGroup import ObstacleGroup
from Project.Entities.Player import Player
from Project.Entities.Bullet import Bullet
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
    @dispatch(Player, ObstacleGroup)
    def getCollisions(player: Player, group: Group):
        result = False
        collisionList = spritecollide(player, group, dokill=False)
        if len(collisionList) > 0:
            filteredCollisionList = filter(lambda obj:
                                           not isinstance(obj, Player),
                                           collisionList)
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
            result = list(filter(lambda obj: isinstance(obj, Bullet), collisionList))
        return result

    @staticmethod
    def filterCollisionList(index, ignorable=None):
        if index == ignorable:
            return False
        else:
            return True
