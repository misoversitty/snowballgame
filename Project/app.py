import pygame
from Entities.Player import Player
from Entities.Bullet import Bullet
from Services.Controls import Controls
from Services.CollisionDetector import CollisionDetector
from Services.Collision import Collision

SCREEN_SIZE = [800, 600]
FPS = 30

NUMBER_OF_PLAYERS = 2

PLAYERS = []
G_ALL_SPRITES = pygame.sprite.Group()
G_PLAYERS = pygame.sprite.Group()
G_BULLETS = pygame.sprite.Group()


def initPlayers(number: int):
    for i in range(number):
        _ = Player(G_ALL_SPRITES, G_PLAYERS, number=i)
        PLAYERS.append(_)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("DudeGame")
clock = pygame.time.Clock()
running = True

initPlayers(number=NUMBER_OF_PLAYERS)
PLAYERS[0].controls = Controls(k_up='w', k_down='s', k_left='a', k_right='d')
PLAYERS[1].controls = Controls(k_up='i', k_down='k', k_left='j', k_right='l')
bullet1 = Bullet(G_ALL_SPRITES, G_BULLETS)
count = 0


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("DudeGame")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    keyReleased = event.dict['unicode']
                    for player in PLAYERS:
                        if keyReleased in player.controls.assignment:
                            side = player.controls.assignment[keyReleased]
                            command = player.__getattribute__(f"stopMove{side}")
                            command.__call__()

                if event.type == pygame.KEYDOWN:
                    keyPressed = event.dict['unicode']
                    for player in PLAYERS:
                        if keyPressed in player.controls.assignment:
                            side = player.controls.assignment[keyPressed]
                            command = player.__getattribute__(f"startMove{side}")
                            command.__call__()

                if event.type == pygame.QUIT:
                    self.running = False
            for player in PLAYERS:
                if player.number == 1:
                    continue
                player.free()
                if collisionContainer := CollisionDetector.isCollided(PLAYERS[0], G_PLAYERS):
                    for collision in collisionContainer:
                        sides = collision.getBlockedSides()
                        for side in sides:
                            print(side)
                            player.state[f"BLOCK_{side}"] = True
            G_ALL_SPRITES.update()

            screen.fill((255, 255, 255))

            G_ALL_SPRITES.draw(screen)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
