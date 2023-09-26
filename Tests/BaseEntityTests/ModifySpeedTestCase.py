import unittest
from Project.Entities.BaseEntity import BaseEntity
import numpy as np


class ModifySpeedTestCase(unittest.TestCase):
    def setUp(self):
        self.entity = BaseEntity(maxSpeed=10, acceleration=[1, 2])
        self.count = 13
        self.standart_start = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], dtype=int)
        self.standart_stop = np.array([11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13], dtype=int)

    def test_modifySpeed_whenMoveUp(self):
        self.entity.startMoveUp()
        for i in range(self.count):
            self.entity.modifySpeed()
            self.assertEqual(self.entity.speed.y, -self.standart_start[i])
        self.entity.stopMoveUp()
        for i in range(self.count):
            self.entity.modifySpeed()
            self.assertEqual(self.entity.speed.y, -self.standart_stop[i])


if __name__ == '__main__':
    unittest.main()
