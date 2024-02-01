from pygame.rect import Rect

from Project.DataStructures.Block import Block


class MapGenerator:
    size = 800, 600
    blocks = []
    symbolNeedToRecord = "12"

    def __init__(self):
        self.readLines("/home/misoversit/PycharmProjects/snowballgame/Project/Map/map.txt")
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
                    block = self.makeBlock(symbol, countX, countY)
                    self.blocks.append(block)

    def isNeedToRecord(self, symbol: str):
        if symbol in self.symbolNeedToRecord:
            return True
        else:
            return False

    def makeBlock(self, symbol: str, countX, countY):
        countX, countY, sizeX, sizeY = self.recalculateSize(countX, countY, 1, 1)
        return Block(symbol, Rect(countX, countY, sizeX, sizeY))

    def recalculateSize(self, startPositionX, startPositionY, recordedSizeX, recordedSizeY):
        return startPositionX * self.scaleX, startPositionY * self.scaleY, recordedSizeX * self.scaleX, recordedSizeY * self.scaleY


generator = MapGenerator()
print('g')
