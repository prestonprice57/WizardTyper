import Effects

# base spell class
class Spell(object):
	def __init__(self):
		self.effects = []
		self.targets = []
		self.casterName = "None"

	# this method will pass any effects to the entity if it is one of the specified targets
	def applyEffectsToEntity(self, entity):
		if self.isTarget(entity):
			for effect in self.effects:
				entity.effects.append(effect)

	# this will check to see if the entity is amount the list of targets
	def isTarget(self, entity):
		for target in self.targets:
			if target == entity.name:
				return True
		return False

# fireball spell class
class Fireball(Spell):
	def __init__(self, multiplier):
		super(Fireball, self).__init__()
		# add the effects
		# the first effectis a quick-hard hit
		duration = 1
		power = 3*multiplier
		self.effects.append(Effects.Burn(duration, power))
		# the second effect is a slow long lasting burn
		duration = 3*multiplier
		power = 1
		self.effects.append(Effects.Burn(duration,power))