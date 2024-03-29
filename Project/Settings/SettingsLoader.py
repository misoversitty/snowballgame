from pathlib import Path

from Project.Globals import SETTINGS_DIRECTORY


class SettingsLoader:
    @staticmethod
    def importFile():
        with open(Path(SETTINGS_DIRECTORY, "Settings.txt"), 'r') as fin:
            lines = [line.strip() for line in fin.readlines()]
        return lines