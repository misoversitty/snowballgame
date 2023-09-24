from math import sqrt


class Speed:
    def __init__(self, maxSpeed: int):
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.max = {"ortho": maxSpeed, "side": int(maxSpeed // sqrt(2))}
