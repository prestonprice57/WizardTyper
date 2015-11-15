import Display
import os
import pygame
import Colliders
import Tags


# stats class contains entity stats like hp and resistances
class Stats(object):

	def __init__(self):
		self.hp = 100
		self._magicPower = 1.0 # percentage
		self._fireResistance = 1.0 # percentage

	# add properties for magicPower and fireResistance


# Entity is the base class for all game entities. (player, crature...)
class Entity(Display.Renderable):

	def __init__(self, sprite_map):
		# Call the parent constructor
		super(Entity, self).__init__(sprite_map, 0)
		self.tile = (0, 0)	# Location in tile units as float
		self.stats = Stats()
		self.dead = False
		self.effects = []
		self.name = None
		self.x = 4
		self.y = 4
		self.dx = 0
		self.dy = 0
		self.speed = 1
		# this is a assignable collider method
		self.collide = Colliders.defaultCollider
		# this is a list of tags that can be assigned for access to the available tags see Tags.py
		self.tags = []

	def render(self, screen):
		''' Override in children'''
		pass

	def hasTag(self, tag):
		return tag in self.tags

	def damage(self, damage):
		self.stats.hp = self.stats.hp - damage
		if self.stats.hp < 1:
			self.dead = True

	def move(self):
		self.x += self.dx
		self.y += self.dy

	def runEffects(self):
		for effect in self.effects:
			if effect.active:
				effect.applyEffect(self)
			else:
				print "effect is no longer active. It has been removed"
				self.effects.remove(effect)

	def update(self):
		self.move()
		self.runEffects()

class Actions(object):
	''' Action state enum'''
	IDLE   = 0
	TAUNT  = 1
	WALK   = 2
	ATTACK = 3
	DIE    = 4
	ACTIVE = 5
	INACTIVE = 6

class Goblin(Entity):

	frames = {
		Actions.IDLE   : [(i * 32,   0) for i in range(10)],
		Actions.TAUNT  : [(i * 32,  32) for i in range(10)],
		Actions.WALK   : [(i * 32,  64) for i in range(10)],
		Actions.ATTACK : [(i * 32,  96) for i in range(10)],
		Actions.DIE    : [(i * 32, 128) for i in range(10)],
	}

	def __init__(self):
		super(Goblin, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'goblin1.png'
				)
			)
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.currentAction = Actions.IDLE

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		screen.blit(
		    pygame.transform.scale(
		        self.sprite_map.subsurface(
		            pygame.Rect(
		                self.frames[self.currentAction][int(self.frame)],
		                (32, 32)
		            ),
		        ),
		        (64, 64)
		    ),
		    (self.x, self.y)
		)

class Cleric(Entity):
	''' Cleric character'''

#!!! Really, there should be a Mobile object that
#!!! this inherits from.  The Mobile object would
#!!! handle movement.  This would set the movement
#!!! speed and deal with the rendering details.

	# This is essentially a static class variable
	# It contains the mapping of frames in the
	# cleric sprite map.
	frames = {
		Actions.IDLE   : [(i * 32,   0) for i in range(10)],
		Actions.TAUNT  : [(i * 32,  32) for i in range(10)],
		Actions.WALK   : [(i * 32,  64) for i in range(10)],
		Actions.ATTACK : [(i * 32,  96) for i in range(10)],
		Actions.DIE    : [(i * 32, 128) for i in range(10)],
	}

	def __init__(self):
		# Call the parent constructor
		super(Cleric, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'cleric spritesheet calciumtrice.png'
				)
			)
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.name = "Cleric"
		self.currentAction = Actions.IDLE
		self.x = 225
		self.y = 225


	def setCurrentAction(self, actionNum):
		if actionNum == 0:
			self.currentAction = Actions.IDLE
		elif actionNum == 1:
			self.currentAction = Actions.TAUNT
		elif actionNum == 2:
			self.currentAction = Actions.WALK
		elif actionNum == 3:
			self.currentAction = Actions.ATTACK
		elif actionNum == 4:
			self.currentAction = Actions.DIE
		else:
			print "Invalid input. Current action not changed."

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		screen.blit(
		    pygame.transform.scale(
		        self.sprite_map.subsurface(
		            pygame.Rect(
		                self.frames[self.currentAction][int(self.frame)],
		                (32, 32)
		            ),
		        ),
		        (64, 64)
		    ),
		    (self.x, self.y)
		)

class Fireball(Entity):
	fireballList = []

	for i in range(4):
		y = i*64
		for j in range(4):
			x = j*64
			fireballList.append((x,y))


	frames = {
		Actions.ACTIVE   : fireballList,
		Actions.INACTIVE : 0
	}

	def __init__(self):
		super(Fireball, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'exp2_0.png'
				)
			)
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.currentAction = Actions.INACTIVE
		self.x = 550
		self.y = 225
		self.animationCompleted = False

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 12

		if self.currentAction == Actions.ACTIVE and not self.animationCompleted:
			screen.blit(
			    pygame.transform.scale(
			        self.sprite_map.subsurface(
			            pygame.Rect(
			                self.frames[self.currentAction][int(self.frame)],
			                (64, 64)
			            ),
			        ),
			        (64, 64)
			    ),
			    (self.x, self.y)
			)
		if int(self.frame) == 11:
			self.animationCompleted = True
			self.currentAction = Actions.INACTIVE

	def setCurrentAction(self, actionNum):
		if actionNum == 0:
			self.currentAction = Actions.INACTIVE
		elif actionNum == 1:
			self.currentAction = Actions.ACTIVE
		else:
			print "Invalid input. Current action not changed."
