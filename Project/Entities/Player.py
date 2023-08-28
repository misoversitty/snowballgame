from random import randint

import pygame
from Project.Services.Facing import Facing
from Project.Services.ImageContainer import ImageContainer
from Project.Services.ImageLoader import ImageLoader
from Project.Services.Speed import Speed


PLAYER_SPEED = 5
PLAYER_INERTIA = [1, 1]
PLAYER_BLINK_PERIOD = 0.5


class Player(pygame.sprite.Sprite):
    imageContainer = ImageContainer(ImageLoader.LoadImage('p1.png'), ImageLoader.LoadImage('p12.png'))

    def __init__(self, *groups, number):
        super().__init__(*groups)
        self.number = number
        self.animCycles = 0
        self.imageKit = self.imageContainer['up']
        self.countWhileMoving = 0
        self.image = self.imageKit[self.countWhileMoving]
        self.rect = self.image.get_rect()
        self.rect.center = (randint(200, 600), randint(300, 500))
        self.controls = None
        self.facing = Facing()
        self.speed = Speed(maxSpeed=PLAYER_SPEED)
        self.acceleration = PLAYER_INERTIA
        self.state = {'MOVING': False,
                      'STARTING_AXIS_X': False,
                      'STARTING_AXIS_Y': False,
                      'SLOWING_AXIS_X': False,
                      'SLOWING_AXIS_Y': False,
                      'PREPARING': False,
                      'SHOOTING': False,
                      'RELOADING': False,
                      'BLOCK_UP': False,
                      'BLOCK_DOWN': False,
                      'BLOCK_LEFT': False,
                      'BLOCK_RIGHT': False}
    def free(self):
        self.state['BLOCK_UP'] = False
        self.state['BLOCK_DOWN'] = False
        self.state['BLOCK_LEFT'] = False
        self.state['BLOCK_RIGHT'] = False

    def startMoveUp(self):
        self.state['STARTING_AXIS_Y'] = True
        self.state['SLOWING_AXIS_Y'] = False
        self.state['MOVING'] = True
        self.speed.dy = -1

    def startMoveDown(self):
        self.state['STARTING_AXIS_Y'] = True
        self.state['SLOWING_AXIS_Y'] = False
        self.state['MOVING'] = True
        self.speed.dy = 1

    def startMoveLeft(self):
        self.state['STARTING_AXIS_X'] = True
        self.state['SLOWING_AXIS_X'] = False
        self.state['MOVING'] = True
        self.speed.dx = -1

    def startMoveRight(self):
        self.state['STARTING_AXIS_X'] = True
        self.state['SLOWING_AXIS_X'] = False
        self.state['MOVING'] = True
        self.speed.dx = 1

    def stopMoveUp(self):
        if self.speed.dy <= 0:
            self.state['STARTING_AXIS_Y'] = False
            self.state['SLOWING_AXIS_Y'] = True
            self.state['MOVING'] = True if self.speed.dx else False
            self.speed.dy = 0

    def stopMoveDown(self):
        if self.speed.dy >= 0:
            self.state['STARTING_AXIS_Y'] = False
            self.state['SLOWING_AXIS_Y'] = True
            self.state['MOVING'] = True if self.speed.dx else False
            self.speed.dy = 0

    def stopMoveLeft(self):
        if self.speed.dx <= 0:
            self.state['STARTING_AXIS_X'] = False
            self.state['SLOWING_AXIS_X'] = True
            self.state['MOVING'] = True if self.speed.dy else False
            self.speed.dx = 0

    def stopMoveRight(self):
        if self.speed.dx >= 0:
            self.state['STARTING_AXIS_X'] = False
            self.state['SLOWING_AXIS_X'] = True
            self.state['MOVING'] = True if self.speed.dy else False
            self.speed.dx = 0

    def calculateFacing(self):
        if self.speed.dx != 0 or self.speed.dy != 0:
            self.facing.x, self.facing.y = self.speed.dx, self.speed.dy

    def pickImageKitAccordingToFacing(self):
        if (self.facing.x, self.facing.y) == (0, -1):
            self.imageKit = self.imageContainer['up']
        if (self.facing.x, self.facing.y) == (0, 1):
            self.imageKit = self.imageContainer['down']
        if (self.facing.x, self.facing.y) == (-1, 0):
            self.imageKit = self.imageContainer['left']
        if (self.facing.x, self.facing.y) == (1, 0):
            self.imageKit = self.imageContainer['right']
        if (self.facing.x, self.facing.y) == (-1, -1):
            self.imageKit = self.imageContainer['up-left']
        if (self.facing.x, self.facing.y) == (1, -1):
            self.imageKit = self.imageContainer['up-right']
        if (self.facing.x, self.facing.y) == (-1, 1):
            self.imageKit = self.imageContainer['down-left']
        if (self.facing.x, self.facing.y) == (1, 1):
            self.imageKit = self.imageContainer['down-right']

    def pickImage(self):
        if self.state['MOVING']:
            self.animCycles += 1
            if self.animCycles >= 30 * PLAYER_BLINK_PERIOD:
                self.animCycles = 0
                self.countWhileMoving += 1
        self.image = self.imageKit[self.countWhileMoving % len(self.imageKit)]

    def checkForCollision(self):
        if a := pygame.sprite.spritecollideany():
            if a[0] and a[1] < 10:
                self.state['BLOCK_UP'] = True
            if a[0] and a[1] > 20:
                self.state['BLOCK_DOWN'] = True
            if a[0] < 10 and a[1]:
                self.state['BLOCK_LEFT'] = True
            if a[0] > 20 and a[1]:
                self.state['BLOCK_RIGHT'] = True
        else:
            self.state['BLOCK_UP'] = False
            self.state['BLOCK_DOWN'] = False
            self.state['BLOCK_LEFT'] = False
            self.state['BLOCK_RIGHT'] = False

    def modifySpeed(self):
        if self.state['STARTING_AXIS_X'] is True:
            self.speed.x += self.speed.dx * self.acceleration[0]
            if abs(self.speed.x) >= self.maxSpeed:
                self.state['STARTING_AXIS_X'] = False

        if self.state['STARTING_AXIS_Y'] is True:
            self.speed.y += self.speed.dy * self.acceleration[0]
            if abs(self.speed.y) >= self.maxSpeed:
                self.state['STARTING_AXIS_Y'] = False

        if self.state['SLOWING_AXIS_X'] is True:
            if self.speed.x > 0:
                self.speed.x += -self.acceleration[1]
            elif self.speed.x < 0:
                self.speed.x += self.acceleration[1]
            else:
                self.state['SLOWING_AXIS_X'] = False
                self.state['STARTING_AXIS_Y'] = True if self.speed.dy else False

        if self.state['SLOWING_AXIS_Y'] is True:
            if self.speed.y > 0:
                self.speed.y += -self.acceleration[1]
            elif self.speed.y < 0:
                self.speed.y += self.acceleration[1]
            else:
                self.state['SLOWING_AXIS_Y'] = False
                self.state['STARTING_AXIS_X'] = True if self.speed.dx else False

    def limitSpeed(self):
        if self.state['BLOCK_UP'] and self.speed.y < 0:
            self.speed.y = 0
        if self.state['BLOCK_DOWN'] and self.speed.y > 0:
            self.speed.y = 0
        if self.state['BLOCK_LEFT'] and self.speed.x < 0:
            self.speed.x = 0
        if self.state['BLOCK_RIGHT'] and self.speed.x > 0:
            self.speed.x = 0
        if abs(self.speed.x) > self.maxSpeed:
            self.speed.x = self.maxSpeed * self.speed.dx
        if abs(self.speed.y) > self.maxSpeed:
            self.speed.y = self.maxSpeed * self.speed.dy

    def modifyCoordinates(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

    def update(self):
        self.calculateFacing()
        self.pickImageKitAccordingToFacing()
        self.pickImage()
        self.maxSpeed = self.speed.module['ortho'] if self.speed.dx * self.speed.dy == 0 else self.speed.module['side']
        self.modifySpeed()
        self.limitSpeed()
        self.modifyCoordinates()
