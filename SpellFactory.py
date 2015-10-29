class SpellFactory(object):
	"""Builds a spell and returns it"""
	def __init__(self, string):
		self.casterString = ""
		self.targetString = ""
		self.spellString  = ""
		self.targetList = []
		self.spellList = []
		self.TYPEKEYWORD = False
		self.ONKEYWORD = False
		self.PARTS = []

		self.__build(string)

	def __build(self, string):
		self.PARTS = string.split(" ")
		print self.PARTS
		#self.__findCaster()
		#self.__findSpells()
		#self.__findTargets()
		self.__findStrings()
		self.__buildSpellList()
		self.__buildTargetList()
		self.__validate()

	def __validate(self):
		if self.spellList.__len__() == 0:
			return False
		elif self.targetList.__len__() == 0:
			return False
		#This will eventually need to validate the casterString exists
		elif self.casterString == "":
			return False

		return True

	def __findStrings(self):
		start = 0
		end = 0

		#Find the keywords cast or block
		while self.PARTS[end] != "cast" and self.PARTS[end] != "block":
			end += 1


		#After they're found, build the caster's string
		for i in range(start, end):
			self.casterString += self.PARTS[i] + " "

		self.casterString[:-1]

		#Adjust the locators
		start = end + 1
		end = start + 1

#########################################################################################

		#Find the keyword "on"
		while self.PARTS[end] != "on":
			end += 1

		#After it's found, build the spell string
		for i in range(start, end):
			self.spellString += self.PARTS[i] + " "

		self.casterString[:-1]

		#Adjust the locators
		start = end + 1
		print "   " + str(start) + ", " + str(end)

##########################################################################################

		for i in range(start, self.PARTS.__len__()):
			self.targetString += self.PARTS[i] + " "
			#print i

		self.targetString[:-1]
		print "CASTER: " + self.casterString
		print "SPELLS: " + self.spellString
		print "TARGETS: " + self.targetString


	def __findCaster(self):
		"""While 'cast'/'block' is not found"""
		part = self.PARTS[0]

		while part != "cast" or part != "block":
			if part == "cast" or part == "block":
				self.TYPEKEYWORD = True

			self.PARTS.remove(part)
			self.casterString += part + " "
			part = self.PARTS[0]


		self.casterString[:-1]
		print self.casterString



	def __findSpells(self):
		if not self.TYPEKEYWORD:
			return

		""""While 'on' is not found"""
		for part in self.PARTS:
			tPart = part.lower()
			self.PARTS.remove(part)

			if tPart == "on":
				self.ONKEYWORD = True
				break

			self.spellString += part + " "

		self.spellString[:-1]


	def __findTargets(self):
		if not self.TYPEKEYWORD and not self.ONKEYWORD:
			print "ERROR"
			return

		for part in self.PARTS:
			print part
			self.targetString += part + " "

		self.targetString[:-1]


	def __buildSpellList(self):
		parts = self.spellString.split(" and ")

		for part in parts:
			#for now we're just going to add strings to the spell list and handle it all later...
			self.spellList.append(part)


	def __buildTargetList(self):
		parts = self.targetString.split(" and ")

		for part in parts:
			#eventually need to add logic to search for the target and verify that it's a valid target
			self.targetList.append(part)




"""		
for part in self.PARTS:
			print part
			tPart = part.lower() #format for easier syntax checking
			self.PARTS.remove(part) #Kick it off the list

			if tPart == "cast" or tPart == "block":				
				self.TYPEKEYWORD = True
				break

			self.casterString += part + " "

		self.casterString[:-1] #Remove the final space
"""