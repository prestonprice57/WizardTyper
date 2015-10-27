import effects

def printStatus(status):
	if status:
		print "\tPass\n"
	else:
		print "\tFail\n"

def testCreatures():
	print "testing creatures"
	printStatus(False)

def testEffects():
	print "testing fireball"
	fire = effects.Fireball(10,20)
	tar = effects.Target(100)
	while fire.effectActive:
		fire.applyEffect(tar)
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
