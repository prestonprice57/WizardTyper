
# effect is a base class for all 
class Effect(object):
	def __init__(self):
		self.timer = 1
		self.power = 1
		self.effectActive = True

	def updateSpellProgress(self):
		if(self.timer > 0):
			self.timer = self.timer - 1
		else:
			self.effectActive = False


class Fireball(Effect):
	def __init__(self, duration, power):
		# call super constuctor
		super(Fireball, self).__init__()
		self.timer = duration
		self.power = power

	def applyEffect(self, target):
		self.updateSpellProgress()
		if self.effectActive:
			target.damage(self.power)
			

class Target(object):

	def __init__(self, hp):
		self.hp = hp
		self.dead = False

	def damage(self, damage):
		self.hp = self.hp - damage
		if self.hp < 1:
			self.dead = True

