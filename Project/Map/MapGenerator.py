from pygame.rect import Rect

class MapGenerator:
    size = 800, 600
    rectangles = []
    symbolNeedToRecord = "1"

    def __init__(self):
        self.readLines("D:\my shit\ProgProjects\snowballgame\Project\Map\map.txt")
        self.calculateScale()
        self.createListOfRectangles()

    def readLines(self, fileName: str):
        with open(fileName, 'r') as fileIn:
            self.lines = [line.strip() for line in fileIn.readlines()]

    def calculateScale(self):
        self.scaleX = self.size[0] // len(self.lines[0])
        self.scaleY = self.size[1] // len(self.lines)

    def createListOfRectangles(self):
        for countY, line in enumerate(self.lines):
            for countX, symbol in enumerate(line):
                if self.isNeedToRecord(symbol):
                    rectangle = self.makeRectangle(symbol, countX, countY)
                    self.rectangles.append(rectangle)

    def isNeedToRecord(self, symbol: str):
        if symbol in self.symbolNeedToRecord:
            return True
        else:
            return False

    def makeRectangle(self, symbol: str, countX, countY):
        countX, countY, sizeX, sizeY = self.recalculateSize(countX, countY, 1, 1)
        return symbol, Rect(countX, countY, sizeX, sizeY)

    def recalculateSize(self, startPositionX, startPositionY, recordedSizeX, recordedSizeY):
        return startPositionX * self.scaleX, startPositionY * self.scaleY, recordedSizeX * self.scaleX, recordedSizeY * self.scaleY


generator = MapGenerator()
print('g')
