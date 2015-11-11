import Effects

# base spell class
class Spell(object):
	def __init__(self):
		self.effects = []
		self.targets = []
		self.casterName = "None"

	# this method will pass any effects to the entity if it is on the targets list
	def applyEffectsToEntity(self, entity):
		if self.isTarget(entity):
			for effect in self.effects:
				entity.effects.append(effect)

	# this will check to see if the entity is amoung the list of targets
	def isTarget(self, entity):
		for target in self.targets:
			if target.lower() == entity.name.lower():
				print target.lower()
				print entity.name.lower()
				return True
		return False

# fireball spell class
class Fireball(Spell):
	def __init__(self, multiplier):
		super(Fireball, self).__init__()
		
		# add the effects

		# the first effect is a quick-hard hit
		duration = 1
		power = 3*multiplier
		self.effects.append(Effects.Burn(duration, power))
		
		# the second effect is a slow long lasting burn
		duration = 3*multiplier
		power = 1
		self.effects.append(Effects.Burn(duration,power))


# lightning spell class
class LightningBolt(Spell):
	def __init__(self, multiplier):
		super(LightningBolt, self).__init__()
		
		# add the effects

		# the first effect is a quick-hard hit
		duration = 1
		power = 5*multiplier
		self.effects.append(Effects.Shock(duration, power))