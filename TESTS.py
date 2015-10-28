#!/usr/bin/python

# This file contains test cases for all of the python classes
# TODO: make the pass and fail messaes green and red

import Effects
import Entities
import Spells

def printStatus(status):
	if status:
		print "\tPass\n"
	else:
		print "\tFail\n"

def testCreatures():
	print "testing creatures"
	printStatus(False)

def testEffects():
	print "testing effects"
	print "testing burn"
	burn = Effects.Burn(10,20)
	tar = Entities.Entity()
	while burn.active:
		burn.applyEffect(tar)
	printStatus(tar.stats.hp == -100 and tar.dead)

def testSpells():
	print "testingSpells"
	# make some targets for the spell
	tar1 = Entities.Entity()
	tar1.stats.hp = 100

	# create the spell and add the list of target names to the spell, normally this would come from the keyboard
	fireball = Spells.Fireball(startingHP/4)
	fireball.targets.append(tar1.name)

	# try to apply the spell to the entities, this should pass on all effects to the listed targets
	fireball.applyEffectsToEntity(tar1)

	while len(tar1.effects) > 0:
		tar1.update()
		print len(tar1.effects)
	
	printStatus(tar1.dead)
	printStatus(False) # this tests needs to check each effect in the spell, but for now we seem okay.

def testSpellbook():
	print "testingSpellbook"
	printStatus(False)

def testArea():
	print "testintArea"
	printStatus(False)


# start tests here
testEffects()
testCreatures()
testSpells()
testSpellbook()
testArea()
