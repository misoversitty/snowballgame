from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


BULLET_SPEED = 5
baseImages = (ImageLoader.loadImage('bullet.png'),)


class Bullet(BaseEntity):
    def __init__(self, **kwargs):
        super().__init__(maxSpeed=BULLET_SPEED, acceleration=[BULLET_SPEED, 0], baseImages=baseImages)
        self.facing = kwargs.get("facing")
        self.speed.dx, self.speed.dy = self.facing.x, self.facing.y
        self.state["MOVING"] = True
        self.state["STARTING_AXIS_X"] = True
        self.state["STARTING_AXIS_Y"] = True


    def update(self):
        super().update()
