# EHandler.py: This is the event handler
# all non registered keys go to a default keyboard function
# Author: Chad Carey, 

import pygame

class EHandler(object):
    
    # constructor, requires a default keyboard function
    def __init__(self, keyboard):
        self.quit = False
        self._keyboard = keyboard
        self._keyMap = {}
    
    # this will register a key to a specific method.
    def registerKey(self, key, method):
        self._keyMap[key] = method
    
    def unregisterKey(self, key):
        if self._keyMap.has_key(key):
            del self._keyMap[key]

    # this method will run all the events to get keyboard input
    # If a key has a method registered to it, it will call that method
    # all unregistered keys use the default keyboard method
    def runEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if self._keyMap.has_key(event.key):
                    self._keyMap[event.key](event)
                else:
                    self._keyboard(event)