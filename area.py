# Area.py: This is meant to be an area of the game
# NOTE: this is in the process of being modified from another game
# Author: Chad Carey, 

class Area:

    def __init__(self):
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.entranceDescription = "you see another room."

    def setAdjacentAreas(self, n, e, s, w):
        self.setAdjacentArea('n',n)
        self.setAdjacentArea('e',e)
        self.setAdjacentArea('s',s)
        self.setAdjacentArea('w',w)

    def setAdjacentArea(self, dir, Area):
        if dir == 'n':
            self.north = Area
        elif dir == 'e':
            self.east = Area
        elif dir == 's':
            self.south = Area
        elif dir == 'w':
            self.west = Area
        else:
            print "you suck at setting your Areas"

    def printOptions(self):
        if self.north != None:
            print "To the north ", self.north.getEntranceDescription()
        if self.east != None:
            print "To the east ", self.east.getEntranceDescription()
        if self.south != None:
            print "To the south ", self.south.getEntranceDescription()
        if self.west != None:
            print "To the west ", self.west.getEntranceDescription()

    def getEntranceDescription(self):
        return self.entranceDescription

    def getArea(self, r):
        if r == 'n':
            return self.north
        elif r == 'e':
            return self.east
        elif r == 's':
            return self.south
        elif r == 'w':
            return self.west
        