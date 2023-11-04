from random import randint
from Project.Entities.Bullet import Bullet
from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


class Player(BaseEntity):
    PLAYER_SPEED = 5
    PLAYER_INERTIA = [1, 1]
    PLAYER_BLINK_PERIOD = 0.5
    BASE_IMAGES = (ImageLoader.loadImage("p1.png"), ImageLoader.loadImage("p12.png"))

    def __init__(self, **kwargs):
        super().__init__(maxSpeed=self.PLAYER_SPEED,
                         acceleration=self.PLAYER_INERTIA,
                         baseImages=self.BASE_IMAGES,
                         coordinates=(randint(200, 600), randint(300, 500)))
        self.No = kwargs.get("number")
        self.control = None
        self.state |= {"PREPARING": False,
                       "SHOOTING": False,
                       "RELOADING": False}
        self.blinkPeriod = 0.5

    def up(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed:
            self.startMoveUp()
        else:
            self.stopMoveUp()

    def down(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed:
            self.startMoveDown()
        else:
            self.stopMoveDown()

    def left(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed:
            self.startMoveLeft()
        else:
            self.stopMoveLeft()

    def right(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed:
            self.startMoveRight()
        else:
            self.stopMoveRight()

    def shoot(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed:
            self.state["SHOOTING"] = True
            print(f"Player #{self.No} did pew-thing")
            b = Bullet(facing=self.facing.copy(),
                       coordinates=self.rect.center)
            b.rect.center = (500, 600)
            return b

    def update(self):
        super().update()
