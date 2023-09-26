from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


class Bullet(BaseEntity):
    BULLET_SPEED = 5
    BASE_IMAGES = (ImageLoader.loadImage('bullet.png'),)

    def __init__(self, **kwargs):
        super().__init__(maxSpeed=self.BULLET_SPEED, acceleration=[0.01, 0], baseImages=self.BASE_IMAGES)
        self.facing = kwargs.get("facing")
        self.start()

    def start(self):
        if self.facing.x == -1:
            self.startMoveLeft()
        elif self.facing.x == 1:
            self.startMoveRight()
        if self.facing.y == -1:
            self.startMoveUp()
        elif self.facing.y == 1:
            self.startMoveDown()

    def update(self):
        super().update()
