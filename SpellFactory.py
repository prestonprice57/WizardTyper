import Spells


class SpellFactory(object):
	"""Builds a spell and returns it"""
	def __init__(self):
		self._spellBook = {
			"fireball":Spells.Fireball,
			"Fireball":Spells.Fireball,
			"lightning bolt":Spells.LightningBolt,
			"LightningBolt":Spells.LightningBolt,
			"heal":Spells.Heal
		}
		self.__reset()

	def __reset(self):
		self.casterString = ""
		self.targetString = ""
		self.spellString  = ""
		self.targetList = []
		self.spellList = []
		self.TYPEKEYWORD = False
		self.ONKEYWORD = False
		self.PARTS = []

	def getSpell(self, caster, spellString, typeSpeed):
		self.__build(spellString)
		caster = caster.lower()
		spells = []
		for spellText in self.spellList:
			if spellText in self._spellBook:
				# get a reference to the class
				spell = self._spellBook[spellText]
				# reset the spell variable to an instaciated version of the class
				spell = spell(typeSpeed)
				spell.targets = self.targetList
				spell.casterName = caster
				spells.append(spell)
		self.__reset()
		return spells

	
	def __build(self, string):
		self.PARTS = string.split(" ")
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
		# while self.PARTS[end] != "cast" and self.PARTS[end] != "block":
		# 	end += 1
		if not "cast" in self.PARTS and not "block" in self.PARTS:
			return

		#After they're found, build the caster's string
		for i in range(start, end):
			self.casterString += self.PARTS[i] + " "

		#Adjust the locators
		start = end + 1
		end = start + 1

		#Find the keyword "on"
		while self.PARTS[end] != "on":
			end += 1

		#After it's found, build the spell string
		for i in range(start, end):
			self.spellString += self.PARTS[i] + " "

		self.casterString = self.casterString[:-1]
		self.spellString = self.spellString[:-1]

		#Adjust the locators
		start = end + 1

		for i in range(start, self.PARTS.__len__()):
			self.targetString += self.PARTS[i] + " "			

		self.targetString = self.targetString[:-1]

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