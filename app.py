import pygame
import math
from random import randint
import pathlib

SCREEN_SIZE = [800, 600]
FPS = 30
DUDE_SPEED = 5
DUDE_INERTIA = [1, 1]
DUDE_BLINK_PERIOD = 0.5
NUMBER_OF_PLAYERS = 2
GAME_DIRECTORY = 'G:/my shit/PYTHONPROJECTS/Tanks'

PLAYERS = []
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()


def loadImage(file: str):
    file = pathlib.Path(GAME_DIRECTORY, file)
    try:
        surface = pygame.image.load(file)
    except FileNotFoundError:
        raise SystemExit(f'Could not load image "{file}".')
    return surface


def rotateImage(img: pygame.image, degrees) -> pygame.image:
    try:
        res = pygame.transform.rotate(img, degrees)
    except pygame.error:
        raise SystemExit(f'Could not rotate image "{img}".')
    return res


class Speed:
    dx = 0
    dy = 0
    x = 0
    y = 0
    module = {'ortho': DUDE_SPEED, 'side': int(DUDE_SPEED // math.sqrt(2))}


class Facing:
    x = 0
    y = -1


class Collision:
    def __init__(self, x: int, y: int):
        self.point = (x, y)


class ImagesContainer:
    def __init__(self, *imgs):
        super().__init__()
        self.dict = {'up': [],
                     'down': [],
                     'left': [],
                     'right': [],
                     'up-left': [],
                     'up-right': [],
                     'down-left': [],
                     'down-right': []}
        for i in imgs:
            self.dict['up'].append(i)
            self.dict['down'].append(rotateImage(i, 180))
            self.dict['left'].append(rotateImage(i, 90))
            self.dict['right'].append(rotateImage(i, 270))
            self.dict['up-left'].append(rotateImage(i, 45))
            self.dict['up-right'].append(rotateImage(i, 325))
            self.dict['down-left'].append(rotateImage(i, 135))
            self.dict['down-right'].append(rotateImage(i, 225))

    def __getitem__(self, item):
        return self.dict[item]


class Dude(pygame.sprite.Sprite):
    images = ImagesContainer(loadImage('p1.png'), loadImage('p12.png'))

    def __init__(self, *groups, number):
        super().__init__(*groups)
        self.number = number
        self.animCycles = 0
        self.imageKit = self.images['up']
        self.countWhileMoving = 0
        self.image = self.imageKit[self.countWhileMoving]
        self.rect = self.image.get_rect()
        self.rect.center = (randint(200, 600), randint(300, 500))
        self.facing = Facing()
        self.speed = Speed()
        self.acceleration = DUDE_INERTIA
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
            self.imageKit = self.images['up']
        if (self.facing.x, self.facing.y) == (0, 1):
            self.imageKit = self.images['down']
        if (self.facing.x, self.facing.y) == (-1, 0):
            self.imageKit = self.images['left']
        if (self.facing.x, self.facing.y) == (1, 0):
            self.imageKit = self.images['right']
        if (self.facing.x, self.facing.y) == (-1, -1):
            self.imageKit = self.images['up-left']
        if (self.facing.x, self.facing.y) == (1, -1):
            self.imageKit = self.images['up-right']
        if (self.facing.x, self.facing.y) == (-1, 1):
            self.imageKit = self.images['down-left']
        if (self.facing.x, self.facing.y) == (1, 1):
            self.imageKit = self.images['down-right']

    def pickImage(self):
        if self.state['MOVING']:
            self.animCycles += 1
            if self.animCycles >= FPS * DUDE_BLINK_PERIOD:
                self.animCycles = 0
                self.countWhileMoving += 1
        self.image = self.imageKit[self.countWhileMoving % len(self.imageKit)]

    def reloadMask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def checkForCollision(self):
        if pygame.sprite.spritecollideany(self, BULLETS):
            print(f'Player #{self.number} collided with bullet')
        for i in PLAYERS:
            if self.number == i.number:
                continue
            if a := pygame.sprite.collide_mask(self, i):
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
        self.reloadMask()
        self.checkForCollision()
        self.maxSpeed = self.speed.module['ortho'] if self.speed.dx * self.speed.dy == 0 else self.speed.module['side']
        self.modifySpeed()
        self.limitSpeed()
        self.modifyCoordinates()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = loadImage('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        pass


class Animation:
    def __init__(self, images: list[pygame.image, ...], duration):
        self.images = images
        self.duration = duration


def initPlayers(number: int):
    for i in range(number):
        _ = Dude(ALL_SPRITES, number=i)
        PLAYERS.append(_)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("DudeGame")
clock = pygame.time.Clock()
running = True

initPlayers(number=NUMBER_OF_PLAYERS)
bullet1 = Bullet(ALL_SPRITES, BULLETS)

count = 0
while running:
    count += 1
    clock.tick(FPS)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            key = event.dict['unicode']
            if key == 'w':
                PLAYERS[0].stopMoveUp()
            if key == 's':
                PLAYERS[0].stopMoveDown()
            if key == 'a':
                PLAYERS[0].stopMoveLeft()
            if key == 'd':
                PLAYERS[0].stopMoveRight()
            if key == 'i':
                PLAYERS[1].stopMoveUp()
            if key == 'k':
                PLAYERS[1].stopMoveDown()
            if key == 'j':
                PLAYERS[1].stopMoveLeft()
            if key == 'l':
                PLAYERS[1].stopMoveRight()

        if event.type == pygame.KEYDOWN:
            key = event.dict['unicode']
            if key == 'w':
                PLAYERS[0].startMoveUp()
            if key == 's':
                PLAYERS[0].startMoveDown()
            if key == 'a':
                PLAYERS[0].startMoveLeft()
            if key == 'd':
                PLAYERS[0].startMoveRight()

            if key == 'i':
                PLAYERS[1].startMoveUp()
            if key == 'k':
                PLAYERS[1].startMoveDown()
            if key == 'j':
                PLAYERS[1].startMoveLeft()
            if key == 'l':
                PLAYERS[1].startMoveRight()

        if event.type == pygame.QUIT:
            running = False

    # Обновление

    prepos = pygame.Surface((50, 50))  # test
    prepos.fill((255, 255, 0))  # test

    ALL_SPRITES.update()

    # Визуализация (сборка)
    screen.fill((255, 255, 255))

    screen.blit(prepos, (400, 300))  # test

    ALL_SPRITES.draw(screen)
    pygame.display.flip()

    if count % 30 == 0:
        # print(dude1.speed.x, dude1.speed.y)
        # print(dude1.state)
        count = 0

pygame.quit()