import pygame

from Project.Services.CollisionDetector import CollisionDetector
from Project.Services.PlayerFactory import PlayerFactory
from Project.Settings.Settings import Settings
from Project.Globals import NUMBER_OF_PLAYERS
from Project.DataStructures.PlayerGroup import PlayerGroup
from Project.DataStructures.BulletGroup import BulletGroup
from Project.DataStructures.ObstacleGroup import ObstacleGroup
from Project.Map.MapGenerator import MapGenerator
from Project.Obstacles.ObstacleFactory import ObstacleFactory


settings = Settings()


PLAYERS = PlayerFactory(count=NUMBER_OF_PLAYERS)
G_ALL_SPRITES = pygame.sprite.Group()
G_PLAYERS = PlayerGroup()
G_BULLETS = BulletGroup()
G_OBSTACLES = ObstacleGroup()


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(settings.screenSettings.getScreenSettings())
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def setUp(self):
        G_ALL_SPRITES.add(p for p in PLAYERS)
        G_PLAYERS.add(p for p in PLAYERS)
        for player in PLAYERS:
            player.control = settings.controlSettings[player.No]
            player.FPS = settings.screenSettings.FPS
        for block in MapGenerator().blocks:
            obstacle = ObstacleFactory(block)
            G_ALL_SPRITES.add(obstacle)
            G_OBSTACLES.add(obstacle)

    def run(self):
        self.setUp()
        while self.running:
            self.clock.tick(settings.screenSettings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    keyReleased = event.dict['unicode']
                    for player in PLAYERS:
                        if keyReleased in player.control.assignment:
                            action = player.control.assignment[keyReleased]
                            command = player.__getattribute__(action)
                            command.__call__(pressed=False)

                if event.type == pygame.KEYDOWN:
                    keyPressed = event.dict['unicode']
                    if keyPressed == 'g':
                        print("Entering Debugggg")
                    for player in PLAYERS:
                        if keyPressed in player.control.assignment:
                            action = player.control.assignment[keyPressed]
                            command = player.__getattribute__(action)
                            thisIsBullet = command.__call__(pressed=True)
                            if thisIsBullet:
                                G_ALL_SPRITES.add(thisIsBullet)
                                G_BULLETS.add(thisIsBullet)

                if event.type == pygame.QUIT:
                    self.running = False
                    
            for player in PLAYERS:
                blockedSides = set()
                if collisionsWithPlayers := CollisionDetector.getCollisions(player, G_PLAYERS):
                    for collision in collisionsWithPlayers:
                        blockedSides |= collision.blockedSides
                if collisionsWithObstacles := CollisionDetector.getCollisions(player, G_OBSTACLES):
                    for collision in collisionsWithObstacles:
                        blockedSides |= collision.blockedSides
                player.free()
                player.block(blockedSides)
                if collisionsWithBullets := CollisionDetector.getCollisions(player, G_BULLETS):
                    for collidedBullet in collisionsWithBullets:
                        collidedBullet.kill()


            G_ALL_SPRITES.update()
            self.screen.fill((255, 255, 255))

            G_ALL_SPRITES.draw(self.screen)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
