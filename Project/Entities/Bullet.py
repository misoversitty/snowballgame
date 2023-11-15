from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


class Bullet(BaseEntity):
    BULLET_SPEED = 5
    BASE_IMAGES = (ImageLoader.loadImage('bullet.png'),)

    def __init__(self, **kwargs):
        super().__init__(maxSpeed=self.BULLET_SPEED,
                         acceleration=[0.01, 0],
                         baseImages=self.BASE_IMAGES,
                         coordinates=kwargs.get("coordinates"))
        self.facing = kwargs.get("facing")
        self.correctCoordinate()
        self.start()

    def correctCoordinate(self):
        if self.facing() == (0, -1):
            self.rect.midright = self.coordinate.x, self.coordinate.y
        elif self.facing() == (0, 1):
            self.rect.midleft = self.coordinate.x, self.coordinate.y
        elif self.facing() == (-1, 0):
            self.rect.midtop = self.coordinate.x, self.coordinate.y
        elif self.facing() == (1, 0):
            self.rect.midbottom = self.coordinate.x, self.coordinate.y

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
