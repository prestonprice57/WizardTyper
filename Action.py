import Parser

class Action(object):

	def __init__(self, spell, target):		
		self.spell = spell
		self.target = target		

	def calculateDamage(self):
		pass #We can eventually pass in a WPM value and handle the calculation here
