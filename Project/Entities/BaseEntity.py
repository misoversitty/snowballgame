import pygame
from pygame.sprite import Sprite
from Project.DataStructures.Speed import Speed
from Project.DataStructures.Acceleration import Acceleration
from Project.DataStructures.Facing import Facing
from Project.DataStructures.ImageContainer import ImageContainer


baseImages = pygame.Surface([30, 30])
baseImages.fill([160, 160, 160])
baseImages = (baseImages,)


class BaseEntity(Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.imageContainer = ImageContainer(*kwargs.get("baseImages", baseImages))
        self.facing = Facing()
        self.speed = Speed(kwargs.get("maxSpeed"))
        self.acceleration = Acceleration(*kwargs.get("acceleration"))
        self.animCycles = 0
        self.imageKit = None
        self.pickImageKitAccordingToFacing()
        self.countWhileMoving = 0
        self.image = self.imageKit[self.countWhileMoving]
        self.rect = self.image.get_rect()
        self.state = {"MOVING": False,
                      "STARTING_AXIS_X": False,
                      "STARTING_AXIS_Y": False,
                      "SLOWING_AXIS_X": False,
                      "SLOWING_AXIS_Y": False,
                      "BLOCK_UP": False,
                      "BLOCK_DOWN": False,
                      "BLOCK_LEFT": False,
                      "BLOCK_RIGHT": False}

    def startMoveUp(self):
        self.state["STARTING_AXIS_Y"] = True
        self.state["SLOWING_AXIS_Y"] = False
        self.state["MOVING"] = True
        self.speed.dy = -1

    def stopMoveUp(self):
        if self.speed.dy <= 0:
            self.state["STARTING_AXIS_Y"] = False
            self.state["SLOWING_AXIS_Y"] = True
            self.state["MOVING"] = True if self.speed.dx else False
            self.speed.dy = 0

    def startMoveDown(self):
        self.state["STARTING_AXIS_Y"] = True
        self.state["SLOWING_AXIS_Y"] = False
        self.state["MOVING"] = True
        self.speed.dy = 1

    def stopMoveDown(self):
        if self.speed.dy >= 0:
            self.state["STARTING_AXIS_Y"] = False
            self.state["SLOWING_AXIS_Y"] = True
            self.state["MOVING"] = True if self.speed.dx else False
            self.speed.dy = 0

    def startMoveLeft(self):
        self.state["STARTING_AXIS_X"] = True
        self.state["SLOWING_AXIS_X"] = False
        self.state["MOVING"] = True
        self.speed.dx = -1

    def stopMoveLeft(self):
        if self.speed.dx <= 0:
            self.state["STARTING_AXIS_X"] = False
            self.state["SLOWING_AXIS_X"] = True
            self.state["MOVING"] = True if self.speed.dy else False
            self.speed.dx = 0

    def startMoveRight(self):
        self.state["STARTING_AXIS_X"] = True
        self.state["SLOWING_AXIS_X"] = False
        self.state["MOVING"] = True
        self.speed.dx = 1

    def stopMoveRight(self):
        if self.speed.dx >= 0:
            self.state["STARTING_AXIS_X"] = False
            self.state["SLOWING_AXIS_X"] = True
            self.state["MOVING"] = True if self.speed.dy else False
            self.speed.dx = 0

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

    def changeImage(self):
        if self.state["MOVING"]:
            self.animCycles += 1
            if self.animCycles >= 30:
                self.animCycles = 0
                self.countWhileMoving += 1
        self.image = self.imageKit[self.countWhileMoving % len(self.imageKit)]

    def modifySpeed(self):
        if self.state["STARTING_AXIS_X"] is True:
            self.speed.x += self.speed.dx * self.acceleration.x["STARTING"]

        if self.state["STARTING_AXIS_Y"] is True:
            self.speed.y += self.speed.dy * self.acceleration.y["STARTING"]

        if self.state["SLOWING_AXIS_X"] is True:
            if self.speed.x > 0:
                self.speed.x += -self.acceleration.x["SLOWING"]
            elif self.speed.x < 0:
                self.speed.x += self.acceleration.x["SLOWING"]
            else:
                self.state["SLOWING_AXIS_X"] = False

        if self.state["SLOWING_AXIS_Y"] is True:
            if self.speed.y > 0:
                self.speed.y += -self.acceleration.y["SLOWING"]
            elif self.speed.y < 0:
                self.speed.y += self.acceleration.y["SLOWING"]
            else:
                self.state["SLOWING_AXIS_Y"] = False

    def limitSpeed(self):
        maxSpeed = self.getMaxSpeed()
        if abs(self.speed.x) > maxSpeed:
            self.speed.x = maxSpeed * self.speed.dx
            self.state["STARTING_AXIS_X"] = False
        else:
            self.state["STARTING_AXIS_X"] = True
        if abs(self.speed.y) > maxSpeed:
            self.speed.y = maxSpeed * self.speed.dy
            self.state["STARTING_AXIS_Y"] = False
        else:
            self.state["STARTING_AXIS_Y"] = True

    def getMaxSpeed(self):
        if self.speed.dx * self.speed.dy == 0:
            return self.speed.max["ortho"]
        else:
            return self.speed.max["side"]

    def modifyCoordinates(self):
        if not self.state["BLOCK_UP"] and self.speed.dy < 0 or not self.state["BLOCK_DOWN"] and self.speed.dy > 0:
            self.rect.y += self.speed.y
        if not self.state["BLOCK_LEFT"] and self.speed.dx < 0 or not self.state["BLOCK_RIGHT"] and self.speed.dx > 0:
            self.rect.x += self.speed.x

    def update(self):
        self.calculateFacing()
        self.pickImageKitAccordingToFacing()
        self.changeImage()
        self.modifySpeed()
        self.limitSpeed()
        self.modifyCoordinates()
