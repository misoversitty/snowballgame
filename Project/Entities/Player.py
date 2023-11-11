from random import randint
from Project.Entities.Bullet import Bullet
from Project.Entities.BaseEntity import BaseEntity
from Project.Services.ImageLoader import ImageLoader


class Player(BaseEntity):
    PLAYER_SPEED = 5
    PLAYER_INERTIA = [1, 1]
    PLAYER_BLINK_PERIOD = 0.5
    PLAYER_RELOAD_TIME = 5
    BASE_IMAGES = (ImageLoader.loadImage("p1.png"), ImageLoader.loadImage("p12.png"))

    def __init__(self, **kwargs):
        super().__init__(maxSpeed=self.PLAYER_SPEED,
                         acceleration=self.PLAYER_INERTIA,
                         baseImages=self.BASE_IMAGES,
                         coordinates=(randint(200, 600), randint(300, 500)))
        self.No = kwargs.get("number")
        self.control = None
        self.state |= {"PREPARING": False,
                       "RELOADING": False,
                       "CAN_SHOOT": True}
        self.blinkPeriod = self.PLAYER_BLINK_PERIOD
        self.reloadingTime = 0

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
        if isPressed and self.state.get("CAN_SHOOT"):
            self.state["RELOADING"] = True
            self.state["CAN_SHOOT"] = False
            print(f"Player #{self.No} did pew-thing")
            bullet = Bullet(facing=self.facing.copy(),
                            coordinates=self.rect.center)
            bullet.rect.center = (500, 600)
            return bullet

    def updateStates(self):
        if self.state.get("RELOADING"):
            self.reloadingTime += 1
        if self.reloadingTime >= self.PLAYER_RELOAD_TIME * self.FPS:
            self.state["RELOADING"] = False
            self.state["CAN_SHOOT"] = True
            self.reloadingTime = 0

    def update(self):
        super().update()
        self.updateStates()
