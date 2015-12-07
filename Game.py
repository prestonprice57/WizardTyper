#!/usr/bin/python

# Game.py: This is the main game file for the WizardTyper game
# Author: Chad Carey, Preston Price

import EHandler
import pygame
import COLOR_CONSTANTS as COLORS
import Display
import Entities
import InputBox
import Area
import SpellFactory
import Tags
import Timer
import names
import random

# game constants
FRAMES_PER_SECOND = 60
SCREEN_SIZE = (512,512)

# initialize pygame
pygame.display.init()
Display.init(SCREEN_SIZE[0],SCREEN_SIZE[1])
Display.register(Area.main_map())

# initialize everything else here
entities = {}
cleric = Entities.Cleric(names.get_first_name().lower())
entities[cleric.name] = cleric

Display.register(cleric)
textBox = InputBox.InputBox()
Display.register(textBox)
spellFactory = SpellFactory.SpellFactory()
timer = Timer.Timer()

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
		textBox.toggle()
		if not textBox.isTyping:
			timer.stopTimer()
			spellText = textBox.currentText
			textBox.clear()
			if len(spellText) > 0:
				words = len(spellText)/4
				minutes = timer.elapsedTime/60
				wpm = words/minutes
				print spellText + " WPM:" + str(wpm)
				spells = spellFactory.getSpell(cleric.name, spellText, wpm)
				# add the spells to the targeted entities
				for spell in spells:
					for target in spell.targets:
						try:
							entities[cleric.name].setCurrentAction(3)
							entities[target].applySpell(spell)
						except:
							print "invalid target"
		else:
			timer.startTimer()


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
	if isKeydown:
		print ""
		for key,entity in entities.iteritems():
			print key + ": " + str(entity.stats.hp)
		print ""

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

# this method will create a new enemy
def generateEnemies(number):
	arrayInit = False
	arr = []

	for i in range(0, number):
		goblin = Entities.Goblin("goblin " + names.get_first_name().lower())

		if arrayInit == False:
			arr = shuffledArray(len(goblin.possibleLocations))
			arrayInit = True
		goblin.x = goblin.possibleLocations[arr[i]][0]
		goblin.y = goblin.possibleLocations[arr[i]][1]

		entities[goblin.name] = goblin
		Display.register(goblin)

def shuffledArray(length):
	i = 0
	arr = []
	for i in range(0,length):
		arr.append(i)
	random.shuffle(arr)

	return arr

# this method will update all entities
def update():
	deadEntities = []
	for key, entity in entities.iteritems():
		entity.update()
		if entity.removeEntity:
			Display.unregister(entity)
			deadEntities.append(key)
	for key in deadEntities:
		del entities[key]
	
	if len(entities) < 2:
		generateEnemies(random.randint(1,6))


# main game loop
clock = pygame.time.Clock()
while not eHandler.quit:

	# run events
	eHandler.runEvents()

	# update all entities
	update()

    # draw
	Display.render()

	# this limits the game to 60 fps
	clock.tick(FRAMES_PER_SECOND)

#game loop ends so we now quit pygame
pygame.quit()
