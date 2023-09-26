import unittest
from Project.DataStructures.Coordinate import Coordinate
import numpy as np


class CoordinateTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Coordinate()
        self.obj.x, self.obj.y = 0, 0
        self.obj.dx, self.obj.dy = 5, 5
        self.obj.d2x, self.obj.d2y = 5, 5

    def test_modifyCoordinate(self):
        rightAnswers = np.array([0, 5, 10, 15, 20], dtype=int)
        for elem in rightAnswers:
            self.assertEqual(self.obj.x, elem)
            self.obj.modifyCoordinate()

    def test_modifySpeed(self):
        rightAnswers = np.array([5, 10, 15, 20, 25], dtype=int)
        for elem in rightAnswers:
            self.assertEqual(self.obj.dx, elem)
            self.obj.modifySpeed()

    def test_update(self):
        rightAnswers = np.array([0, 5, 15, 30, 50, 75], dtype=int)
        for elem in rightAnswers:
            self.assertEqual(self.obj.x, elem)
            self.obj.update()


if __name__ == '__main__':
    unittest.main()
