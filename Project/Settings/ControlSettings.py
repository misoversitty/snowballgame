from Project.Services.Singleton import Singleton
from Project.Settings.Control import Control


class ControlSettings(metaclass=Singleton):
    def __init__(self, settingsLines: dict[dict, ...]):
        self.dict = {}
        for playerNo, actionKeyPairs in settingsLines.items():
            self.dict[playerNo] = Control()
            for action, assignedKey in actionKeyPairs.items():
                self.dict[playerNo].set(key=assignedKey, action=action)

    def __getitem__(self, item):
        return self.dict[item]
