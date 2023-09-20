from Project.Services.Singleton import Singleton
from Project.DataStructures.ScreenSize import ScreenSize


class ScreenSettings(metaclass=Singleton):
    def __init__(self, settingsLines):
        self.screenSize = ScreenSize(width=settingsLines["Screen_Width"], height=settingsLines["Screen_Height"])
        self.FPS = settingsLines["FPS"]

    def getScreenSettings(self):
        return self.screenSize.width, self.screenSize.height
