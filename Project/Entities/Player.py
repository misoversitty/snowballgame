from random import randint
from Project.Entities.Bullet import Bullet
from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


PLAYER_SPEED = 5
PLAYER_INERTIA = [1, 1]
PLAYER_BLINK_PERIOD = 0.5
baseImages = (ImageLoader.loadImage("p1.png"), ImageLoader.loadImage("p12.png"))


class Player(BaseEntity):

    def __init__(self, **kwargs):
        super().__init__(maxSpeed=PLAYER_SPEED, acceleration=PLAYER_INERTIA, baseImages=baseImages)
        self.No = kwargs.get("number")
        self.rect.center = (randint(200, 600), randint(300, 500))
        self.control = None
        self.state |= {"PREPARING": False,
                       "SHOOTING": False,
                       "RELOADING": False}

    def free(self):
        self.state["BLOCK_UP"] = False
        self.state["BLOCK_DOWN"] = False
        self.state["BLOCK_LEFT"] = False
        self.state["BLOCK_RIGHT"] = False

    def block(self, sides):
        for side in sides:
            self.state[f"BLOCK_{side}"] = True

    def up(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            self.startMoveUp()
        else:
            self.stopMoveUp()

    def down(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            self.startMoveDown()
        else:
            self.stopMoveDown()

    def left(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            self.startMoveLeft()
        else:
            self.stopMoveLeft()

    def right(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            self.startMoveRight()
        else:
            self.stopMoveRight()

    def shoot(self, **kwargs):
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            self.state["SHOOTING"] = True
            print(f"Player #{self.No} did pew-thing")
            b = Bullet(facing=self.facing.copy())
            b.rect.center = self.rect.center
            return b

    def update(self):
        super().update()
