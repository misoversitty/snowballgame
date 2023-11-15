from pygame.rect import Rect


class Block:
    def __init__(self, symbol: str, rectangle: Rect):
        self.type = symbol
        self.rect = rectangle

    def getTopLeft(self):
        return self.rect.topleft

    def getSize(self):
        return self.rect.width, self.rect.height
