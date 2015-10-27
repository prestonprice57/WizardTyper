

class Stats(object):

	def __init__(self):
		self.hp = 100
		self._magicPower = 1.0 # percentage
		self._fireResistance = 1.0 # percentage

	def __init__(self, hp, magicPower, fireResistance):
		self.hp = hp
		self._magicPower = magicPower
		self._fireResistance = fireResistance

	# add properties for magicPower and fireResistance


class Entity(object):

	def __init__(self):
		self.stats = Stats
		self.dead = False

	def __init__(self, stats):
		self.stats = stats
		self.dead = False

	def damage(self, damage):
		self.hp = self.stats.hp - damage
		if self.stats.hp < 1:
			self.dead = True
