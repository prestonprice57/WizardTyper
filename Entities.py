

class Stats(object):

	def __init__(self):
		self.hp = 100
		self._magicPower = 1.0 # percentage
		self._fireResistance = 1.0 # percentage

	# add properties for magicPower and fireResistance


class Entity(object):

	def __init__(self):
		self.stats = Stats()
		self.dead = False
		self.effects = []
		self.name = None

	def damage(self, damage):
		self.stats.hp = self.stats.hp - damage
		if self.stats.hp < 1:
			self.dead = True

	def update(self):
		for effect in self.effects:
			effect.applyEffect(self)
