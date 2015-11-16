import Entities
import Display
import SpellAnimations

# effect is a base class for all effects
class Effect(object):
	def __init__(self):
		self.timer = 1
		self.power = 1
		self.active = True
		self.animation = None
		self.animationRegistered = False

	def __del__(self):
		if self.animationRegistered:
			Display.unregister(self.animation)
			print "animition unregistered"

	def updateSpellProgress(self):
		if(self.timer > 0):
			self.timer = self.timer - 1
		else:
			self.active = False

	def applyEffect(self, entity):
		pass

	def updateAnimation(self, entity):
		if self.animation:
			if not self.animationRegistered:
				print "animation registered"
				Display.register(self.animation)
				self.animationRegistered = True
			self.animation.updateAnimation(entity)


# burn is a damage effect
class Burn(Effect):
	def __init__(self, duration, power):
		# call super constuctor
		super(Burn, self).__init__()
		self.timer = duration
		self.power = power
		self.animation = SpellAnimations.FireAnimation()

	def __del__(self):
		super(Burn, self).__del__()


	def applyEffect(self, entity):
		self.updateSpellProgress()
		if self.active:
			entity.damage(self.power)
			self.updateAnimation(entity)


# burn is a damage effect
class Shock(Effect):
	def __init__(self, duration, power):
		# call super constuctor
		super(Shock, self).__init__()
		self.timer = duration
		self.power = power

	def applyEffect(self, entity):
		self.updateSpellProgress()
		if self.active:
			entity.damage(self.power)
			

# burn is a damage effect
class Heal(Effect):
	def __init__(self, duration, power):
		# call super constuctor
		super(Heal, self).__init__()
		self.timer = duration
		self.power = power
		if self.power > 0:
			self.power = -self.power

	def __del__(self):
		super(Heal, self).__del__()


	def applyEffect(self, entity):
		self.updateSpellProgress()
		if self.active:
			entity.damage(self.power)
			self.updateAnimation(entity)