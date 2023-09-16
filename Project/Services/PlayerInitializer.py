import numpy as np
from Project.Entities.Player import Player


class PlayerInitializer:
    def __new__(cls, count):
        players = np.array([Player(number=i) for i in np.arange(count)], dtype=Player)
        return players
