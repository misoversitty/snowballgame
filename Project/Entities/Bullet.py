from pygame.sprite import Sprite
from Project.Services.ImageLoader import ImageLoader
from Project.DataStructures.ImageContainer import ImageContainer
from Project.DataStructures.Speed import Speed
from Project.DataStructures.Facing import Facing


BULLET_SPEED = 5

class Bullet(Sprite):
    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.imageContainer = ImageContainer(ImageLoader.loadImage('bullet.png'))
        #self.imageKit = None
        self.facing = kwargs.get("facing")
        self.pickImageKitAccordingToFacing()
        self.image = self.imageKit[0]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        self.speed = Speed(maxSpeed=BULLET_SPEED)

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

    def update(self):
        pass
