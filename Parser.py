"""
	Dev notes:
		I wasn't really sure if this should be applied into a class or not.
		I figure we can build an Action and apply these functions
"""

import Action

class Parser(object):
	def __init__(self, commands):
		self.commandList = commands.split(", ")
		self.ActionList = []

		for command in self.commandList:
			if not self.validate(command):
				continue

			spell = self.parseSpell(command)
			command = command.replace(spell, "SPELL")
			target = self.parseTarget(command)

			#Add it on
			self.ActionList.append(Action.Action(spell, target))

	"""Returns the spell from a command"""
	def parseSpell(self, input):
		parts = input.split(" ")

		i = 1
		spell = ""

		while parts[i] != "on" or i >= parts.__len__:
			if parts[i + 1] == "on":
				spell += parts[i]
			else:
				spell += parts[i] + " "
			i += 1

		if self.isValidSpell(spell):
			return spell
		else:
			return "INVALID"

	"""Returns the target from a command"""
	#This function retrieves the target from a command
	#Input is modified such that it is more easily parsed
	#The spell (in event of multiple words) must be replaced to "SPELL"
	#if not previously done.
	def parseTarget(self, input):
		parts = input.split(" ")	

		while True:
			word = parts[0]
			parts.remove(word)

			num = parts.__len__()

			if (word == "on"):
				break
			if num == 0:
				break
		
		target = " ".join(parts)

		if self.isValidTarget(target):
			return target
		else:
			return "INVALID"


	"""Return whether a command is valid"""
	def validate(self, input):	
		parts = input.split(" ")

		if parts[0] != "Cast":
			#print "No \"cast\" keyword found"
			return False

		i = 1

		while i < (parts.__len__() - 1):
			if parts[i] == "on":
				return True
			i += 1

		#print ("No \"on\" keyword found")
		return False

	#This will search a list/dictionary for the target
	def isValidTarget(self, target):
		return True

	#This will search a list/dictionary for the spell
	def isValidSpell(self, spell):
		return True
