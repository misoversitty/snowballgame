from Project.Services.ImageLoader import ImageLoader
import numpy as np
from pygame import Surface

class ImageContainer:
    def __init__(self, *images):
        super().__init__()
        length = len(images)
        self.dict = {
            'up': np.empty(shape=[length], dtype=Surface),
            'down': np.empty(shape=[length], dtype=Surface),
            'left': np.empty(shape=[length], dtype=Surface),
            'right': np.empty(shape=[length], dtype=Surface),
            'up-left': np.empty(shape=[length], dtype=Surface),
            'up-right': np.empty(shape=[length], dtype=Surface),
            'down-left': np.empty(shape=[length], dtype=Surface),
            'down-right': np.empty(shape=[length], dtype=Surface)
        }
        for count, image in enumerate(images):
            self.dict['up'][count] = image
            self.dict['down'][count] = ImageLoader.rotateImage(image, 180)
            self.dict['left'][count] = ImageLoader.rotateImage(image, 90)
            self.dict['right'][count] = ImageLoader.rotateImage(image, 270)
            self.dict['up-left'][count] = ImageLoader.rotateImage(image, 45)
            self.dict['up-right'][count] = ImageLoader.rotateImage(image, 325)
            self.dict['down-left'][count] = ImageLoader.rotateImage(image, 135)
            self.dict['down-right'][count] = ImageLoader.rotateImage(image, 225)

    def __getitem__(self, item):
        return self.dict[item]
