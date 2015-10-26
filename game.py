# Game.py: This is the main game file for the WizardTyper game
# Author: Chad Carey, 


import EHandler
import pygame
import COLOR_CONSTANTS as COLORS

# game constants
FRAMES_PER_SECOND = 60
SCREEN_SIZE = (800,600)

# initialize pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Wizard Typer")

# initialize everything else here


# initializing the eHandler, You must give the eHandler a default keyboard function
def keyboard(event):
	key = event.key
	print key
eHandler = EHandler.EHandler(keyboard)

# callback methods for the eHandler go here
# NOTE: all callback methods take an pygame.event a a parameter
def quit(event):
	eHandler.quit = True

# add methods to EHandler here
# the following is an example
# eHandler.registerKey(pygame.K_a, exampleCallbackMethod)
eHandler.registerKey(pygame.K_ESCAPE, quit)

# main game loop
clock = pygame.time.Clock()
while not eHandler.quit:
	eHandler.runEvents()

	# clear and draw again
	screen.fill(COLORS.BACKGROUND)

    # all drawing happens here



	# flip the back buffer
	pygame.display.flip()
	# this limits the game to 60 fps
	clock.tick(FRAMES_PER_SECOND)

#game loop ends so we now quit pygame
pygame.quit()