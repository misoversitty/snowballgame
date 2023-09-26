from copy import copy


class Facing:
    def __init__(self, x=0, y=-1):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x, self.y

    def copy(self):
        return copy(self)
