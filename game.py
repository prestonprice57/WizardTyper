#!/usr/bin/python

# Game.py: This is the main game file for the WizardTyper game
# Author: Chad Carey, Preston Price

import EHandler
import pygame
import COLOR_CONSTANTS as COLORS
import display
import Entities
import Inputbox
import Area
import SpellFactory
import Tags
import Timer

# game constants
FRAMES_PER_SECOND = 60
SCREEN_SIZE = (800,600)

# initialize pygame
pygame.display.init()
display.init(800,600)
display.register(Area.main_map())

# initialize everything else here
cleric = Entities.Cleric()
goblin = Entities.Goblin()
fireball = Entities.Fireball()
display.register(goblin)
display.register(cleric)
textBox = Inputbox.InputBox()
display.register(textBox)
spellFactory = SpellFactory.SpellFactory()
timer = Timer.Timer()
display.register(fireball)

# initializing the eHandler, You must give the eHandler a default keyboard function
def keyboard(event, isKeydown):
	key = event.key
	if textBox.isTyping and isKeydown:
		try:
			textBox.currentText += chr(key)
		except:
			# this happens if shift, ctrl, alt, ect... is pressed.
			pass
eHandler = EHandler.EHandler(keyboard)

# callback methods for the eHandler go here
# NOTE: all callback methods take an pygame.event a a parameter
def quit(event, isKeydown):
	eHandler.quit = True

def enterKey(event, isKeydown):
	if isKeydown:
		if not textBox.isTyping:
			timer.startTimer()
		else:
			timer.stopTimer()
		textBox.toggle()
		spellText = textBox.currentText
		textBox.clear()
		if len(spellText) > 0:
			print spellText + ": " + str(timer.elapsedTime)
			spells = spellFactory.getSpell(cleric.name, spellText, 1)
			for spell in spells:
				spell.applyEffectsToEntity(cleric)


def moveLeft(event, isKeydown):
	if isKeydown:
		cleric.dx = -cleric.speed
		cleric.setCurrentAction(2)
	else:
		cleric.dx = 0.0
		cleric.setCurrentAction(0)

def moveRight(event, isKeydown):
	if isKeydown:
		cleric.dx = cleric.speed
		cleric.setCurrentAction(2)
	else:
		cleric.dx = 0.0
		cleric.setCurrentAction(0)

def moveUp(event, isKeydown):
	if isKeydown:
		cleric.dy = -cleric.speed
		cleric.setCurrentAction(2)
	else:
		cleric.dy = 0.0
		cleric.setCurrentAction(0)

def moveDown(event, isKeydown):
	if isKeydown:
		cleric.dy = cleric.speed
		cleric.setCurrentAction(2)
	else:
		cleric.dy = 0.0
		cleric.setCurrentAction(0)

def printHP(event, isKeydown):
	if isKeydown: print cleric.stats.hp

# add methods to EHandler here
# the following is an example
# eHandler.registerKey(pygame.K_a, exampleCallbackMethod)
eHandler.registerKey(pygame.K_ESCAPE, quit)
eHandler.registerKey(pygame.K_LEFT, moveLeft)
eHandler.registerKey(pygame.K_RIGHT, moveRight)
eHandler.registerKey(pygame.K_UP, moveUp)
eHandler.registerKey(pygame.K_DOWN, moveDown)
eHandler.registerKey(pygame.K_RETURN, enterKey)
eHandler.registerKey(pygame.K_BACKSPACE, textBox.undo)
eHandler.registerKey(pygame.K_TAB, printHP)

# main game loop
clock = pygame.time.Clock()
while not eHandler.quit:

	# run events
	eHandler.runEvents()

	# update objects
	cleric.update()

    # draw
	display.render()

	# this limits the game to 60 fps
	clock.tick(FRAMES_PER_SECOND)

#game loop ends so we now quit pygame
pygame.quit()
