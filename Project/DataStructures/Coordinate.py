class Coordinate:
    def __init__(self):
        self.x = None
        self.y = None

        self.dx = None
        self.dy = None

        self.target_dx = None
        self.target_dy = None

        self.d2x = None
        self.d2y = None

    def modifyCoordinate(self):
        self.x += self.dx
        self.y += self.dy

    def modifySpeed(self):
        if self.dx != self.target_dx:
            self.dx += self.d2x
        if self.dy != self.target_dy:
            self.dy += self.d2y

    def limitSpeed(self):
        if self.dx > abs(self.target_dx) and self.d2x > 0:
            self.dx = self.target_dx
        elif self.dx < -abs(self.target_dx) and self.d2x < 0:
            self.dx = -self.target_dx
        if self.dy > abs(self.target_dy) and self.d2y > 0:
            self.dy = self.target_dy
        elif self.dy < -abs(self.target_dy) and self.d2y < 0:
            self.dy = -self.target_dy

    def limitAcceleration(self):
        if self.dx == self.target_dx:
            self.d2x = 0
        if self.dy == self.target_dy:
            self.d2y = 0

    def update(self):
        self.modifyCoordinate()
        self.modifySpeed()
        self.limitSpeed()
        self.limitAcceleration()
