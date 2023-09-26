import pygame
from pygame.sprite import Sprite
from Project.DataStructures.Coordinate import Coordinate
from math import sqrt
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
        self.animCycles = 0
        self.imageKit = None
        self.pickImageKitAccordingToFacing()
        self.countWhileMoving = 0
        self.image = self.imageKit[self.countWhileMoving]
        self.rect = self.image.get_rect()
        self.state = {"MOVING": False,
                      "BLOCK_UP": False,
                      "BLOCK_DOWN": False,
                      "BLOCK_LEFT": False,
                      "BLOCK_RIGHT": False}

        self.coordinate = Coordinate()
        self.coordinate.x, self.coordinate.y = kwargs.get("coordinates", (0, 0))
        self.coordinate.dx, self.coordinate.dy = 0, 0
        self.coordinate.target_dx, self.coordinate.target_dy = 0, 0
        self.coordinate.d2x, self.coordinate.d2y = 0, 0

        self.maxSpeed = {"orthogonal": kwargs.get("maxSpeed"),
                         "side": kwargs.get("maxSpeed") // sqrt(2)}
        self.maxAcceleration = {"STARTING": kwargs.get("acceleration")[0],
                                "STOPPING": kwargs.get("acceleration")[-1]}

    def startMoveUp(self):
        self.coordinate.target_dy = -self.maxSpeed["orthogonal"]
        self.coordinate.d2y = -self.maxAcceleration["STARTING"]
        if self.coordinate.target_dx > 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = -self.maxSpeed["orthogonal"]
        if self.coordinate.target_dx < 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = self.maxSpeed["orthogonal"]

    def stopMoveUp(self):
        if self.coordinate.dy < 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = self.maxAcceleration["STOPPING"]

    def startMoveDown(self):
        self.coordinate.target_dy = self.maxSpeed["orthogonal"]
        self.coordinate.d2y = self.maxAcceleration["STARTING"]
        if self.coordinate.target_dx > 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = -self.maxSpeed["orthogonal"]
        elif self.coordinate.target_dx < 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = self.maxSpeed["orthogonal"]

    def stopMoveDown(self):
        if self.coordinate.dy > 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = -self.maxAcceleration["STOPPING"]

    def startMoveLeft(self):
        self.coordinate.target_dx = -self.maxSpeed["orthogonal"]
        self.coordinate.d2x = -self.maxAcceleration["STARTING"]
        if self.coordinate.target_dy > 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = -self.maxSpeed["orthogonal"]
        elif self.coordinate.target_dy < 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = self.maxSpeed["orthogonal"]

    def stopMoveLeft(self):
        if self.coordinate.dx < 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = self.maxAcceleration["STOPPING"]

    def startMoveRight(self):
        self.coordinate.target_dx = self.maxSpeed["orthogonal"]
        self.coordinate.d2x = self.maxAcceleration["STARTING"]
        if self.coordinate.target_dy > 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = -self.maxSpeed["orthogonal"]
        elif self.coordinate.target_dy < 0:
            self.coordinate.target_dy = 0
            self.coordinate.d2y = self.maxSpeed["orthogonal"]

    def stopMoveRight(self):
        if self.coordinate.dx > 0:
            self.coordinate.target_dx = 0
            self.coordinate.d2x = self.maxAcceleration["STOPPING"]

    def calculateFacing(self):
        if self.coordinate.dx != 0 or self.coordinate.dy != 0:
            try:
                self.facing.x = self.coordinate.dx // abs(self.coordinate.dx)
            except ZeroDivisionError:
                self.facing.x = 0
            try:
                self.facing.y = self.coordinate.dy // abs(self.coordinate.dy)
            except ZeroDivisionError:
                self.facing.y = 0

    def pickImageKitAccordingToFacing(self):
        if self.facing() == (0, -1):
            self.imageKit = self.imageContainer["up"]
        elif self.facing() == (0, 1):
            self.imageKit = self.imageContainer["down"]
        elif self.facing() == (-1, 0):
            self.imageKit = self.imageContainer["left"]
        elif self.facing() == (1, 0):
            self.imageKit = self.imageContainer["right"]
        elif self.facing() == (-1, -1):
            self.imageKit = self.imageContainer["up-left"]
        elif self.facing() == (1, -1):
            self.imageKit = self.imageContainer["up-right"]
        elif self.facing() == (-1, 1):
            self.imageKit = self.imageContainer["down-left"]
        elif self.facing() == (1, 1):
            self.imageKit = self.imageContainer["down-right"]

    def changeImage(self):
        if self.coordinate.dx + self.coordinate.dy != 0:
            self.animCycles += 1
            if self.animCycles >= 30:
                self.animCycles = 0
                self.countWhileMoving += 1
        self.image = self.imageKit[self.countWhileMoving % len(self.imageKit)]


    def update(self):
        self.calculateFacing()
        self.pickImageKitAccordingToFacing()
        self.changeImage()
        self.coordinate.update()
        self.rect.center = self.coordinate.x, self.coordinate.y
