#!/usr/bin/python

# Game.py: This is the main game file for the WizardTyper game
# Author: Chad Carey, 


import EHandler
import pygame
import COLOR_CONSTANTS as COLORS
import display
import Entities
import inputbox
import pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

# game constants
FRAMES_PER_SECOND = 60
SCREEN_SIZE = (800,600)

# initialize pygame
pygame.display.init()
display.init(800,600)
display.register(Entities.main_map())

# initialize everything else here
cleric = Entities.Cleric()
cleric.set_location(cleric.x,cleric.y)
display.register(cleric)
#def inputBox(screen):
#	pygame.draw_rect(screen, (0,0,0), ((screen.get_width() / 2) - 100, )
#		)

# initializing the eHandler, You must give the eHandler a default keyboard function
isTyping = False
def keyboard(event):
	key = event.key

	if key == 13:
		print "ENTER WAS PRESSED"
		msg = inputbox.ask(screen, "")     #This here works, but we could probably make it work better for us...
		print msg

	#if isTyping:
	#	if key == pygame.K_ENTER:
	#		isTyping = False
	#		text = textBox.clear()
	#		spell = spellBook.getSpell(text)
	#		area.castSpell(spell)
	#	textBox.enterText(key)
	#elif key == pygame.K_ENTER:
	#	isTyping = True
	print key
eHandler = EHandler.EHandler(keyboard)

# callback methods for the eHandler go here
# NOTE: all callback methods take an pygame.event a a parameter
def quit(event):
	eHandler.quit = True


def moveLeft(event):
	cleric.x-=.2
	cleric.set_location(cleric.x,cleric.y)
	display.register(cleric)

def moveRight(event):
	cleric.x+=.2
	cleric.set_location(cleric.x,cleric.y)
	display.register(cleric)

def moveUp(event):
	cleric.y-=.2
	cleric.set_location(cleric.x,cleric.y)
	display.register(cleric)

def moveDown(event):
	cleric.y+=.2
	cleric.set_location(cleric.x,cleric.y)
	display.register(cleric)

# add methods to EHandler here
# the following is an example
# eHandler.registerKey(pygame.K_a, exampleCallbackMethod)
eHandler.registerKey(pygame.K_ESCAPE, quit)
eHandler.registerKey(pygame.K_LEFT, moveLeft)
eHandler.registerKey(pygame.K_RIGHT, moveRight)
eHandler.registerKey(pygame.K_UP, moveUp)
eHandler.registerKey(pygame.K_DOWN, moveDown)
# main game loop
clock = pygame.time.Clock()
while not eHandler.quit:
	eHandler.runEvents()

	# clear and draw again
	#screen.fill(COLORS.BACKGROUND)
	display.render()
    # all drawing happens here



	# flip the back buffer
	pygame.display.flip()
	# this limits the game to 60 fps
	clock.tick(FRAMES_PER_SECOND)

#game loop ends so we now quit pygame
pygame.quit()