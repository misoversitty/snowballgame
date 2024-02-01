from Project.Obstacles.Obstacle import Obstacle
from Project.Obstacles.DestructibleObstacle import DestructibleObstacle
from Project.DataStructures.Block import Block


class ObstacleFactory:
    def __new__(cls, block: Block):
        if block.type == '1':
            return Obstacle(block=block)
        elif block.type == '2':
            return DestructibleObstacle(block=block)
