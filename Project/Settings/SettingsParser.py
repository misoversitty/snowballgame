from Project.Services.Singleton import Singleton

class SettingsParser(metaclass=Singleton):
    def __init__(self, lines: list[str, ...]):
        self.rawLines = lines
        self.purifiedLines = self.parse()
        self.purifiedLines["CONTROLS"] = self.cleanControlSettingsLines()


    def parse(self):
        res = {}
        for line in self.rawLines:
            if SettingsParser.isCategory(line):
                categoryName = SettingsParser.makeCategoryName(line)
                res[categoryName] = {}
            elif categoryName in res:
                key, *trash, value = line.split()
                try:
                    value = int(value)
                except ValueError:
                    pass
                res[categoryName][key] = value
        return res


    @staticmethod
    def isCategory(s):
        if s[0] == "[" and s[-1] == "]":
            return True
        else:
            return False


    @staticmethod
    def makeCategoryName(s):
        return s.strip("[]")


    def cleanControlSettingsLines(self):
        res = {}
        for rawString, assignedKey in self.purifiedLines["CONTROLS"].items():
            playerNo, assignedAction = rawString.split("_")
            playerNo = int(playerNo[-1])
            assignedAction = assignedAction.lower()
            if playerNo in res:
                res[playerNo][assignedAction] = assignedKey
            else:
                res[playerNo] = {assignedAction: assignedKey}
        return res


    def getScreenSettingsLines(self):
        return self.purifiedLines["SCREEN"]


    def getControlSettingsLines(self):
        return self.purifiedLines["CONTROLS"]
