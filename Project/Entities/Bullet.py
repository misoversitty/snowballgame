from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


BULLET_SPEED = 5
baseImages = (ImageLoader.loadImage('bullet.png'),)


class Bullet(BaseEntity):
    def __init__(self, **kwargs):
        super().__init__(maxSpeed=BULLET_SPEED, acceleration=[0.01, 0], baseImages=baseImages)
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
