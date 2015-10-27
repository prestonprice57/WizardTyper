# Area.py: This is meant to be an area of the game
# NOTE: this is in the process of being modified from another game
# Author: Chad Carey, 

class Area:

    def __init__(self):
        self._north = None
        self._east = None
        self._south = None
        self._west = None
        self._entranceDescription = "you see another room."

    def __init__(self, n, s, e, w):
        self._north = n
        self._south = s
        self._east = e
        self._west = w

    def setAdjacentAreas(self, n, s, e, w):
        self._north = n
        self._south = s
        self._east = e
        self._west = w

    def printOptions(self):
        if self._north != None:
            print "To the north ", self._north.entranceDescription
        if self._south != None:
            print "To the south ", self._south.entranceDescription
        if self._east != None:
            print "To the east ", self._east.entranceDescription
        if self._west != None:
            print "To the west ", self._west.entranceDescription