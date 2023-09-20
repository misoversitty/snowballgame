import pygame
from Entities.Bullet import Bullet
from Project.Settings.Control import Control
from Services.CollisionDetector import CollisionDetector
from Services.PlayerInitializer import PlayerInitializer
from Project.Settings.Settings import Settings


settings = Settings()

SCREEN_SIZE = [800, 600]
FPS = 30

NUMBER_OF_PLAYERS = 2

PLAYERS = PlayerInitializer(count=NUMBER_OF_PLAYERS)
G_ALL_SPRITES = pygame.sprite.Group()
G_PLAYERS = pygame.sprite.Group()
G_BULLETS = pygame.sprite.Group()


def setUp():
    PLAYERS[0].control = Control(k_up='w', k_down='s', k_left='a', k_right='d')
    PLAYERS[1].control = Control(k_up='i', k_down='k', k_left='j', k_right='l')
    G_ALL_SPRITES.add(p for p in PLAYERS)
    G_PLAYERS.add(p for p in PLAYERS)


setUp()
bullet1 = Bullet(G_ALL_SPRITES, G_BULLETS)
count = 0


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(settings.screenSettings.getScreenSettings())
        pygame.display.set_caption("DudeGame")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(settings.screenSettings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    keyReleased = event.dict['unicode']
                    for player in PLAYERS:
                        if keyReleased in player.control.assignment:
                            side = player.control.assignment[keyReleased]
                            command = player.__getattribute__(f"stopMove{side}")
                            command.__call__()

                if event.type == pygame.KEYDOWN:
                    keyPressed = event.dict['unicode']
                    for player in PLAYERS:
                        if keyPressed in player.control.assignment:
                            side = player.control.assignment[keyPressed]
                            command = player.__getattribute__(f"startMove{side}")
                            command.__call__()

                if event.type == pygame.QUIT:
                    self.running = False
                    
            for player in PLAYERS:
                blockedSides = set()
                if collisionsWithPlayers := CollisionDetector.getCollisions(player, G_PLAYERS):
                    for collision in collisionsWithPlayers:
                        blockedSides |= collision.blockedSides
                else:
                    player.free()
                player.block(blockedSides)


            G_ALL_SPRITES.update()

            self.screen.fill((255, 255, 255))

            G_ALL_SPRITES.draw(self.screen)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
