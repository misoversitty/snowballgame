from Project.Services.ImageLoader import ImageLoader

class ImageContainer:
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
            self.dict['down'].append(ImageLoader.rotateImage(i, 180))
            self.dict['left'].append(ImageLoader.rotateImage(i, 90))
            self.dict['right'].append(ImageLoader.rotateImage(i, 270))
            self.dict['up-left'].append(ImageLoader.rotateImage(i, 45))
            self.dict['up-right'].append(ImageLoader.rotateImage(i, 325))
            self.dict['down-left'].append(ImageLoader.rotateImage(i, 135))
            self.dict['down-right'].append(ImageLoader.rotateImage(i, 225))

    def __getitem__(self, item):
        return self.dict[item]