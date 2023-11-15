from Project.Obstacles.Obstacle import Obstacle


class DestructibleObstacle(Obstacle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lives = 10
        self.image.fill([205, 133, 63])