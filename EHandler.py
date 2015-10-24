import pygame

class EHandler(object):
    
    def __init__(self, keyboard):
        self.quit = False
        self._keyboard = keyboard
        self._keyMap = {}
    
    def registerKey(self, key, method):
        self._keyMap[key] = method
    
    def unregisterKey(self, key):
        if self._keyMap.has_key(key):
            del self._keyMap[key]

    # this method will run all the registered events
    def runEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if self._keyMap.has_key(event.key):
                    self._keyMap[event.key](event)
                else:
                    self._keyboard(event)