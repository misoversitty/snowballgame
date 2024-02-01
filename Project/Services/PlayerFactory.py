import numpy as np

from Project.Entities.Player import Player


class PlayerFactory:
    def __new__(cls, count):
        players = np.array([Player(number=i) for i in np.arange(count)], dtype=Player)
        return players
