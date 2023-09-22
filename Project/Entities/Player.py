from random import randint
from pygame.sprite import Sprite
from Project.Entities.Bullet import Bullet
from Project.Services.ImageLoader import ImageLoader
from Project.DataStructures.Facing import Facing
from Project.DataStructures.ImageContainer import ImageContainer
from Project.DataStructures.Speed import Speed


PLAYER_SPEED = 5
PLAYER_INERTIA = [1, 1]
PLAYER_BLINK_PERIOD = 0.5


class Player(Sprite):
    imageContainer = ImageContainer(ImageLoader.loadImage("p1.png"), ImageLoader.loadImage("p12.png"))

    def __init__(self, *groups, number):
        super().__init__(*groups)
        self.No = number
        self.animCycles = 0
        self.imageKit = self.imageContainer["up"]
        self.countWhileMoving = 0
        self.image = self.imageKit[self.countWhileMoving]
        self.rect = self.image.get_rect()
        self.rect.center = (randint(200, 600), randint(300, 500))
        self.control = None
        self.facing = Facing()
        self.speed = Speed(maxSpeed=PLAYER_SPEED)
        self.acceleration = PLAYER_INERTIA
        self.state = {"MOVING": False,
                      "STARTING_AXIS_X": False,
                      "STARTING_AXIS_Y": False,
                      "SLOWING_AXIS_X": False,
                      "SLOWING_AXIS_Y": False,
                      "PREPARING": False,
                      "SHOOTING": False,
                      "RELOADING": False,
                      "BLOCK_UP": False,
                      "BLOCK_DOWN": False,
                      "BLOCK_LEFT": False,
                      "BLOCK_RIGHT": False}

    def free(self):
        self.state["BLOCK_UP"] = False
        self.state["BLOCK_DOWN"] = False
        self.state["BLOCK_LEFT"] = False
        self.state["BLOCK_RIGHT"] = False

    def block(self, sides):
        for side in sides:
            self.state[f"BLOCK_{side}"] = True

    def up(self, **kwargs):
        def __startMoveUp():
            self.state["STARTING_AXIS_Y"] = True
            self.state["SLOWING_AXIS_Y"] = False
            self.state["MOVING"] = True
            self.speed.dy = -1

        def __stopMoveUp():
            if self.speed.dy <= 0:
                self.state["STARTING_AXIS_Y"] = False
                self.state["SLOWING_AXIS_Y"] = True
                self.state["MOVING"] = True if self.speed.dx else False
                self.speed.dy = 0

        isPressed = kwargs.get("pressed")
        if isPressed is True:
            __startMoveUp()
        else:
            __stopMoveUp()

    def down(self, **kwargs):
        def __startMoveDown():
            self.state["STARTING_AXIS_Y"] = True
            self.state["SLOWING_AXIS_Y"] = False
            self.state["MOVING"] = True
            self.speed.dy = 1

        def __stopMoveDown():
            if self.speed.dy >= 0:
                self.state["STARTING_AXIS_Y"] = False
                self.state["SLOWING_AXIS_Y"] = True
                self.state["MOVING"] = True if self.speed.dx else False
                self.speed.dy = 0

        isPressed = kwargs.get("pressed")
        if isPressed is True:
            __startMoveDown()
        else:
            __stopMoveDown()

    def left(self, **kwargs):
        def __startMoveLeft():
            self.state["STARTING_AXIS_X"] = True
            self.state["SLOWING_AXIS_X"] = False
            self.state["MOVING"] = True
            self.speed.dx = -1

        def __stopMoveLeft():
            if self.speed.dx <= 0:
                self.state["STARTING_AXIS_X"] = False
                self.state["SLOWING_AXIS_X"] = True
                self.state["MOVING"] = True if self.speed.dy else False
                self.speed.dx = 0

        isPressed = kwargs.get("pressed")
        if isPressed is True:
            __startMoveLeft()
        else:
            __stopMoveLeft()

    def right(self, **kwargs):
        def __startMoveRight():
            self.state["STARTING_AXIS_X"] = True
            self.state["SLOWING_AXIS_X"] = False
            self.state["MOVING"] = True
            self.speed.dx = 1

        def __stopMoveRight():
            if self.speed.dx >= 0:
                self.state["STARTING_AXIS_X"] = False
                self.state["SLOWING_AXIS_X"] = True
                self.state["MOVING"] = True if self.speed.dy else False
                self.speed.dx = 0

        isPressed = kwargs.get("pressed")
        if isPressed is True:
            __startMoveRight()
        else:
            __stopMoveRight()

    def shoot(self, **kwargs):
        def __shoot():
            self.state["SHOOTING"] = True
            print(f"Player #{self.No} did pew-thing")
            b = Bullet(facing=self.facing)
            b.rect.center = self.rect.center
            return b
        isPressed = kwargs.get("pressed")
        if isPressed is True:
            return __shoot()

    def calculateFacing(self):
        if self.speed.dx != 0 or self.speed.dy != 0:
            self.facing.x, self.facing.y = self.speed.dx, self.speed.dy

    def pickImageKitAccordingToFacing(self):
        if (self.facing.x, self.facing.y) == (0, -1):
            self.imageKit = self.imageContainer["up"]
        elif (self.facing.x, self.facing.y) == (0, 1):
            self.imageKit = self.imageContainer["down"]
        elif (self.facing.x, self.facing.y) == (-1, 0):
            self.imageKit = self.imageContainer["left"]
        elif (self.facing.x, self.facing.y) == (1, 0):
            self.imageKit = self.imageContainer["right"]
        elif (self.facing.x, self.facing.y) == (-1, -1):
            self.imageKit = self.imageContainer["up-left"]
        elif (self.facing.x, self.facing.y) == (1, -1):
            self.imageKit = self.imageContainer["up-right"]
        elif (self.facing.x, self.facing.y) == (-1, 1):
            self.imageKit = self.imageContainer["down-left"]
        elif (self.facing.x, self.facing.y) == (1, 1):
            self.imageKit = self.imageContainer["down-right"]

    def pickImage(self):
        if self.state["MOVING"]:
            self.animCycles += 1
            if self.animCycles >= 30 * PLAYER_BLINK_PERIOD:
                self.animCycles = 0
                self.countWhileMoving += 1
        self.image = self.imageKit[self.countWhileMoving % len(self.imageKit)]

    def modifySpeed(self):
        if self.state["STARTING_AXIS_X"] is True:
            self.speed.x += self.speed.dx * self.acceleration[0]
            if abs(self.speed.x) >= self.maxSpeed:
                self.state["STARTING_AXIS_X"] = False

        if self.state["STARTING_AXIS_Y"] is True:
            self.speed.y += self.speed.dy * self.acceleration[0]
            if abs(self.speed.y) >= self.maxSpeed:
                self.state["STARTING_AXIS_Y"] = False

        if self.state["SLOWING_AXIS_X"] is True:
            if self.speed.x > 0:
                self.speed.x += -self.acceleration[1]
            elif self.speed.x < 0:
                self.speed.x += self.acceleration[1]
            else:
                self.state["SLOWING_AXIS_X"] = False
                self.state["STARTING_AXIS_Y"] = True if self.speed.dy else False

        if self.state["SLOWING_AXIS_Y"] is True:
            if self.speed.y > 0:
                self.speed.y += -self.acceleration[1]
            elif self.speed.y < 0:
                self.speed.y += self.acceleration[1]
            else:
                self.state["SLOWING_AXIS_Y"] = False
                self.state["STARTING_AXIS_X"] = True if self.speed.dx else False

    def limitSpeed(self):
        if abs(self.speed.x) > self.maxSpeed:
            self.speed.x = self.maxSpeed * self.speed.dx
        if abs(self.speed.y) > self.maxSpeed:
            self.speed.y = self.maxSpeed * self.speed.dy

    def modifyCoordinates(self):
        if not self.state["BLOCK_UP"] and self.speed.dy < 0 or not self.state["BLOCK_DOWN"] and self.speed.dy > 0:
            self.rect.y += self.speed.y
        if not self.state["BLOCK_LEFT"] and self.speed.dx < 0 or not self.state["BLOCK_RIGHT"] and self.speed.dx > 0:
            self.rect.x += self.speed.x

    def update(self):
        self.calculateFacing()
        self.pickImageKitAccordingToFacing()
        self.pickImage()
        self.maxSpeed = self.speed.module["ortho"] if self.speed.dx * self.speed.dy == 0 else self.speed.module["side"]
        self.modifySpeed()
        self.limitSpeed()
        self.modifyCoordinates()
