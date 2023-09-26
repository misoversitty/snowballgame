import unittest
from Project.Entities.BaseEntity import BaseEntity


class CalculateFacingTestCase(unittest.TestCase):
    def setUp(self):
        self.entity = BaseEntity(maxSpeed=5, acceleration=[1, 1])

    def test_calculateFacing_lookingUp(self):
        self.entity.startMoveUp()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, 0)
        self.assertEqual(self.entity.facing.y, -1)

    def test_calculateFacing_lookingDown(self):
        self.entity.startMoveDown()
        self.entity.coordinate.update()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, 0)
        self.assertEqual(self.entity.facing.y, 1)

    def test_calculateFacing_lookingLeft(self):
        self.entity.startMoveLeft()
        self.entity.coordinate.update()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, -1)
        self.assertEqual(self.entity.facing.y, 0)

    def test_calculateFacing_lookingRight(self):
        self.entity.startMoveRight()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, 1)
        self.assertEqual(self.entity.facing.y, 0)

    def test_calculateFacing_lookingUpLeft(self):
        self.entity.startMoveUp()
        self.entity.startMoveLeft()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, -1)
        self.assertEqual(self.entity.facing.y, -1)

    def test_calculateFacing_lookingUpRight(self):
        self.entity.startMoveUp()
        self.entity.startMoveRight()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, 1)
        self.assertEqual(self.entity.facing.y, -1)

    def test_calculateFacing_lookingDownLeft(self):
        self.entity.startMoveDown()
        self.entity.startMoveLeft()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, -1)
        self.assertEqual(self.entity.facing.y, 1)

    def test_calculateFacing_lookingDownRight(self):
        self.entity.startMoveDown()
        self.entity.startMoveRight()
        self.entity.calculateFacing()
        self.assertEqual(self.entity.facing.x, 1)
        self.assertEqual(self.entity.facing.y, 1)


if __name__ == '__main__':
    unittest.main()
