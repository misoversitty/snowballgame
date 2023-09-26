import unittest
from Project.Entities.BaseEntity import BaseEntity


class LimitSpeedTestCase(unittest.TestCase):
    def setUp(self):
        self.entity = BaseEntity(maxSpeed=10, acceleration=[1, 1])
        self.timeToGetMaxSpeed = int(self.entity.speed.max["ortho"] // self.entity.acceleration.y["STARTING"] + 1)

    def test_limitSpeedWhenMovingUp(self):
        self.entity.startMoveUp()
        for _ in range(self.timeToGetMaxSpeed + 5):
            self.entity.modifySpeed()
        self.entity.limitSpeed()
        self.assertEqual(abs(self.entity.speed.y), self.entity.speed.max["ortho"])

    def test_limitSpeedWhenMovingDown(self):
        self.entity.startMoveDown()
        for _ in range(self.timeToGetMaxSpeed + 5):
            self.entity.modifySpeed()
        self.entity.limitSpeed()
        self.assertEqual(abs(self.entity.speed.y), self.entity.speed.max["ortho"])

    def test_limitSpeedWhenMovingLeft(self):
        self.entity.startMoveLeft()
        for _ in range(self.timeToGetMaxSpeed + 5):
            self.entity.modifySpeed()
        self.entity.limitSpeed()
        self.assertEqual(abs(self.entity.speed.x), self.entity.speed.max["ortho"])

    def test_limitSpeedWhenMovingRight(self):
        self.entity.startMoveRight()
        for _ in range(self.timeToGetMaxSpeed + 5):
            self.entity.modifySpeed()
        self.entity.limitSpeed()
        self.assertEqual(abs(self.entity.speed.x), self.entity.speed.max["ortho"])


if __name__ == '__main__':
    unittest.main()
