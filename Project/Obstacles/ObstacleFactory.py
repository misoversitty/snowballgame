from Project.Obstacles.Obstacle import Obstacle
from Project.Obstacles.DestructibleObstacle import DestructibleObstacle
from Project.DataStructures.Block import Block


class ObstacleFactory:
    def __init__(self):
        pass

    def makeObstacle(self, block: Block):
        if block.type == '1':
            return Obstacle(block=block)
        elif block.type == '2':
            return DestructibleObstacle(block=block)