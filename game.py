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


# callback methods for the eHandler go here
# NOTE: all callback methods take an pygame.event a a parameter
def keyboard(event):
	key = event.key
	print key

# initializing the eHandler
eHandler = EHandler.EHandler(keyboard)

# add methods to EHandler here
# the following is an example
# eHandler.registerKey(pygame.K_a, exampleCallbackMethod)


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