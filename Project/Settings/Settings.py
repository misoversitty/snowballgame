from Project.Settings.SettingsLoader import SettingsLoader
from Project.Settings.SettingsParser import SettingsParser
from Project.Settings.ScreenSettings import ScreenSettings
from Project.Settings.ControlSettings import ControlSettings
from Project.Services.Singleton import Singleton


class Settings(metaclass=Singleton):
    def __init__(self):
        settingsLinesFromFile = SettingsLoader.importFile()
        parser = SettingsParser(settingsLinesFromFile)
        screenSettingsLines = parser.getScreenSettingsLines()
        self.screenSettings = ScreenSettings(screenSettingsLines)
        controlSettingsLines = parser.getControlSettingsLines()
        self.controlSettings = ControlSettings(controlSettingsLines)
