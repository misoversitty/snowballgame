from Project.Services.Singleton import Singleton

class SettingsParser(metaclass=Singleton):
    def __init__(self, lines: list[str, ...]):
        self.rawLines = lines
        self.purifiedLines = self.parse()

    def parse(self):
        res = {}
        for line in self.rawLines:
            if SettingsParser.isCategory(line):
                categoryName = SettingsParser.makeCategoryName(line)
                res[categoryName] = {}
            else:
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


    def getScreenSettingsLines(self):
        return self.purifiedLines["SCREEN"]


    def getControlSettingsLines(self):
        return self.purifiedLines["CONTROLS"]
