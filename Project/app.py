import pygame
from Project.Services.CollisionDetector import CollisionDetector
from Project.Services.PlayerInitializer import PlayerInitializer
from Project.Settings.Settings import Settings
from Project.Globals import NUMBER_OF_PLAYERS
from Project.DataStructures.PlayerGroup import PlayerGroup
from Project.DataStructures.BulletGroup import BulletGroup
from Project.DataStructures.ObstacleGroup import ObstacleGroup
from Project.Map.MapGenerator import MapGenerator


settings = Settings()


PLAYERS = PlayerInitializer(count=NUMBER_OF_PLAYERS)
G_ALL_SPRITES = pygame.sprite.Group()
G_PLAYERS = PlayerGroup()
G_BULLETS = BulletGroup()
G_OBSTACLES = ObstacleGroup()



mapGen = MapGenerator()
for rect in mapGen.rectangles:
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.Surface((rect[1][2], rect[1][3]))
    sprite.image.fill([205, 133, 63])
    sprite.rect = sprite.image.get_rect()
    sprite.rect.topleft = rect[1][0], rect[1][1]
    G_ALL_SPRITES.add(sprite)
    G_OBSTACLES.add(sprite)

def setUp():
    G_ALL_SPRITES.add(p for p in PLAYERS)
    G_PLAYERS.add(p for p in PLAYERS)
    for player in PLAYERS:
        player.control = settings.controlSettings[player.No]
        player.FPS = settings.screenSettings.FPS

count = 0


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(settings.screenSettings.getScreenSettings())
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        setUp()
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
