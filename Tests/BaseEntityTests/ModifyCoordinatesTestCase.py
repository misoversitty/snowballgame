import unittest
from Project.Entities.BaseEntity import BaseEntity
import numpy as np


class ModifyCoordinatesTestCase(unittest.TestCase):
    def setUp(self):
        self.entity = BaseEntity(maxSpeed=10, acceleration=[1, 1])

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
