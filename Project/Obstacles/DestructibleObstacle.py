from Project.Obstacles.Obstacle import Obstacle


class DestructibleObstacle(Obstacle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
