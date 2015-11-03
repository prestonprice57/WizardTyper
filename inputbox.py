# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import display
import COLOR_CONSTANTS as COLORS


class InputBox(display.Renderable):

    def __init__(self):
        pygame.font.init()
        self.currentText = ""
        self.z_index = 10
        self.isTyping = False

  # render the display box with text here
    def render(self, screen):
        "Print a message in a box in the middle of the screen"
        if self.isTyping:
            box1 = (0, screen.get_height() - 31, screen.get_width(), 30)
            textLocation = (box1[0], box1[1] + (box1[3]/3))
            fontobject = pygame.font.Font(None,18)
            pygame.draw.rect(screen, COLORS.BLACK, box1 , 0)
            if len(self.currentText) > 0:
                screen.blit(fontobject.render(self.currentText, 1, COLORS.WHITE), textLocation)

    def toggle(self):
        self.isTyping = not self.isTyping

    def clear(self):
        self.currentText = ""

    def undo(self, event = None, isKeydown = True):
        if isKeydown:
            self.currentText = self.currentText[:-1]