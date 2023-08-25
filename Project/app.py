import pygame
from Entities.Player import Player
from Entities.Bullet import Bullet
from Services.Controls import Controls
from Services.CollisionDetector import CollisionDetector

SCREEN_SIZE = [800, 600]
FPS = 30

NUMBER_OF_PLAYERS = 2

PLAYERS = []
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()


def initPlayers(number: int):
    for i in range(number):
        _ = Player(ALL_SPRITES, number=i)
        PLAYERS.append(_)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("DudeGame")
clock = pygame.time.Clock()
running = True

initPlayers(number=NUMBER_OF_PLAYERS)
PLAYERS[0].controls = Controls(['w', 's', 'a', 'd'])
PLAYERS[1].controls = Controls(['i', 'k', 'j', 'l'])
bullet1 = Bullet(ALL_SPRITES, BULLETS)

count = 0
while running:
    count += 1
    clock.tick(FPS)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            key = event.dict['unicode']
            for player in PLAYERS:
                if key == player.controls.up:
                    player.stopMoveUp()
                if key == player.controls.down:
                    player.stopMoveDown()
                if key == player.controls.left:
                    player.stopMoveLeft()
                if key == player.controls.right:
                    player.stopMoveRight()

        if event.type == pygame.KEYDOWN:
            key = event.dict['unicode']
            for player in PLAYERS:
                if key == player.controls.up:
                    player.startMoveUp()
                if key == player.controls.down:
                    player.startMoveDown()
                if key == player.controls.left:
                    player.startMoveLeft()
                if key == player.controls.right:
                    player.startMoveRight()

        if event.type == pygame.QUIT:
            running = False

    # Обновление
    ALL_SPRITES.update()

    # Визуализация (сборка)
    screen.fill((255, 255, 255))

    ALL_SPRITES.draw(screen)
    pygame.display.flip()

    if count % 30 == 0:
        # print(dude1.speed.x, dude1.speed.y)
        # print(dude1.state)
        count = 0

pygame.quit()
