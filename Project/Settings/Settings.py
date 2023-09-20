from Project.Settings.SettingsLoader import SettingsLoader
from Project.Settings.SettingsParser import SettingsParser
from Project.Settings.ScreenSettings import ScreenSettings
from Project.Settings.ControlSettings import ControlSettings
from Project.Services.Singleton import Singleton


class Settings(metaclass=Singleton):
    settingsLinesFromFile = SettingsLoader.importFile()
    parser = SettingsParser(settingsLinesFromFile)
    screenSettingsLines = parser.getScreenSettingsLines()
    screenSettings = ScreenSettings(screenSettingsLines)
    controlSettingsLines = parser.getControlSettingsLines()
    controlSettings = ControlSettings(controlSettingsLines)
