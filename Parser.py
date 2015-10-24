"""
	Dev notes:
		I wasn't really sure if this should be applied into a class or not.
		I figure we can build an Action and apply these functions
"""

def parseInput(input):
	#make all characters lower case
	input = input.lower()

	#Look for commas (",") in the string
	commands = input.split(", ")

	#Iterate through the commands
	for command in commands:
		pass

#Parse the spell from a string
#	Input --> The message being sent in
#	returns 'spell' from the input.  This should be the text between 'cast' and 'on'
def parseSpell(input):
	if not validate(input):
		return "NOT VALID"

	#Split the string into a list for easier analyzing
	parts = input.split(" ")

	i = 1
	spell = ""

	#Get the name of the spell from the parts
	while parts[i] != "on":
		if parts[i + 1] == "on":
			spell += parts[i]
		else:
			spell += parts[i] + " "
		i += 1

	#TODO: Validate the spell when we have a list of spells
	return spell 

def parseTarget(input):
	if not validate(input):
		return "NOT VALID"

	parts = input.split(" ")

	#The target will always be the last section of the string
	action = parts[0] + " " + parts[1] + " " + parts[2] + " "
	return input.replace(action, "") #TODO: Validate the target when we have a list of targets

#Validates a string for proper syntax, does no checking for valid target or spell
#	Input --> The message being sent in
#	Returns true 
def validate(input):
	input = input.lower()
	#Break apart the input based on spaces to inspect each part
	parts = input.split(" ")

	if parts[0] != "cast":
		print "No cast keyword found"
		return False

	i = 1

	#Search until the second to last element.
	#If nothing is found at the second to last element, we can assume that no "on" word
	#was found, OR the input is just bad.
	while i < (parts.__len__() - 1):
		if parts[i] == "on":
			return True #When we find it, go ahead and return true on valid syntax
		i += 1

	return False

#This will search a list/dictionary for the target
def isValidTarget(target):
	return True

#This will search a list/dictionary for the spell
def isValidSpell(spell):
	return True