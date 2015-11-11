#!/usr/bin/python
# This file contains test cases for all of the python classes

# the following changes the colors of the terminal to make fails easier to see
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

import Effects
import Entities
import Spells
import SpellFactory
import Tags

# this will print colored pass / fails
def printStatus(status):
	if status:
		print Back.GREEN + Fore.BLACK + "\tPass"
	else:
		print Back.RED + Fore.WHITE + "\tFail"
	print "\n"
	return status

def testCreatures():
	print "testing creatures"
	printStatus(False)

def testEffects():
	print "testing effects"
	print "testing burn"
	burn = Effects.Burn(10,20)
	tar = Entities.Entity(None)
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

def testSpellFactory(msg, str1, str2, str3, expSpellList, expTargetList):
	print "testingSpellFactory"

	print "TESTING STRING \"" + msg + "\""
	sf = SpellFactory.SpellFactory()
	spells = sf.getSpell("player", msg, 1)

	print "testing the returned spell array"
	print "\tarray length == ", len(spells)
	print "\texpected length == ", len(expSpellList)
	printStatus(len(spells) == len(expSpellList))

	print "testing the returned spell array's targets"
	for spell in spells:
		print "\ttesting a spell"
		spellTargets = spell.targets
		printStatus(len(spellTargets) == len(expTargetList))

# start tests here
testEffects()
testCreatures()
#testSpells()
testSpellbook()
testArea()

msg1 = "Player cast fireball on skeleton"
msg2 = "Player cast fireball and lightning bolt on skeleton"
msg3 = "Player cast fireball on skeleton 1 and skeleton 2"
msg4 = "Player cast fireball and lightning bolt on skeleton 1 and skeleton 2"

testSpellFactory(msg1, "Player", "fireball", "skeleton", ["fireball"], ["skeleton"])
testSpellFactory(msg2, "Player", "fireball and lightning bolt", "skeleton", ["fireball", "lightning bolt"], ["skeleton"])
testSpellFactory(msg3, "Player", "fireball", "skeleton 1 and skeleton 2", ["fireball"], ["skeleton 1", "skeleton 2"])
testSpellFactory(msg4, "Player", "fireball and lightning bolt", "skeleton 1 and skeleton 2", ["fireball", "lightning bolt"], ["skeleton 1", "skeleton 2"])
