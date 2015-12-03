import Effects

# base spell class
class Spell(object):
	def __init__(self):
		self.effects = []
		self.targets = []
		self.casterName = "None"

# fireball spell class
class Fireball(Spell):
	def __init__(self, multiplier):
		super(Fireball, self).__init__()
		
		# add the effects

		# the first effect is a quick-hard hit
		duration = 1
		power = 3*multiplier
		#self.effects.append(Effects.Burn(duration, power))
		
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


# fireball spell class
class Heal(Spell):
	def __init__(self, multiplier):
		super(Heal, self).__init__()
		
		# add the effects

		# the first effect is a quick heal
		duration = 2
		power = 10*multiplier
		self.effects.append(Effects.Heal(duration, power))

