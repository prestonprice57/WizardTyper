#!/usr/bin/python

import Effects
import Entities

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
	tar = Entities.Entity(100)
	while burn.effectActive:
		burn.applyEffect(tar)
	printStatus(tar.hp == -100 and tar.dead)

def testSpells():
	print "testingSpells"
	printStatus(False)

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
