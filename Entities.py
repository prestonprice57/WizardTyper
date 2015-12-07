import Display
import os
import pygame
import Colliders
import Tags
import COLOR_CONSTANTS as COLORS

# stats class contains entity stats like hp and resistances
class Stats(object):

	def __init__(self):
		self.hp = 1000
		self.maxHP = 10000
		self._magicPower = 1.0 # percentage
		self._magicResistance = 1.0 # percentage

	# add properties for magicPower and fireResistance


# Entity is the base class for all game entities. (player, crature...)
class Entity(Display.Renderable):

	def __init__(self, sprite_map, name):
		# Call the parent constructor
		super(Entity, self).__init__(sprite_map, 1)
		self.tile = (0, 0)	# Location in tile units as float
		self.stats = Stats()
		self.dead = False
		self.effects = []
		self.name = name
		self.x = 4
		self.y = 4
		self.dx = 0
		self.dy = 0
		self.speed = 1
		# this is a assignable collider method
		self.collide = Colliders.defaultCollider
		# this is a list of tags that can be assigned for access to the available tags see Tags.py
		self.tags = []
		self.effectApplied = True
		self.removeEntity = False

	def applySpell(self, spell):
		for effect in spell.effects:
			print "added spell"
			self.effects.append(effect.copy())

	def displayText(self, screen, txt, x, y):
		fontobject = pygame.font.Font(None,20)
		screen.blit(fontobject.render(txt, 1, COLORS.BLACK), (x-len(txt),y))

	def render(self, screen):
		''' Override in children'''
		pass

	def hasTag(self, tag):
		return tag in self.tags

	def damage(self, damage):
		self.stats.hp = self.stats.hp - damage
		if self.stats.hp < 1:
			self.dead = True
		if self.stats.hp > self.stats.maxHP:
			self.stats.hp = self.stats.maxHP

	def move(self):
		self.x += self.dx
		self.y += self.dy

	def runEffects(self):
		for effect in self.effects:
			if effect.active:
				effect.applyEffect(self)
				effectApplied = True
			else:
				print "effect is no longer active. It has been removed"
				#effectApplied = False
				self.effects.remove(effect)
				self.isDead()

	def update(self):
		self.move()
		self.runEffects()

	def isDead(self):
		if self.dead:
			self.setCurrentAction(4)

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

	def __init__(self, name):
		super(Goblin, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'goblin1.png'
				)
			),
			name
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.currentAction = Actions.IDLE
		self.x = 60
		self.y = 60
		self.possibleLocations = [(60,60),(170,60),(280,60),(390,60),
								  (60,120),(170,120),(280,120),(390,120),
								  (80,180),(360,180),
								  (60,300),(170,300),(280,300),(390,300),
								  (60,360),(170,360),(280,360),(390,360)]

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		if self.currentAction == Actions.IDLE:
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
		elif self.currentAction == Actions.DIE:
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
			if int(self.frame) == 9:
				self.removeEntity = True
				"""screen.blit(
				    pygame.transform.scale(
				        self.sprite_map.subsurface(
				            pygame.Rect(
				                self.frames[4][9],
				                (32, 32)
				            ),
				        ),
				        (64, 64)
				    ),
				    (self.x, self.y)
				)
				self.currentAction = Actions.WALK"""

		self.displayText(screen, self.name, self.x, self.y+16)

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

	def __init__(self, name):
		# Call the parent constructor
		super(Cleric, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'cleric spritesheet calciumtrice.png'
				)
			),
			name
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.currentAction = Actions.IDLE
		self.x = 225
		self.y = 225

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		if self.currentAction == Actions.IDLE:
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
		elif self.currentAction == Actions.ATTACK:
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
			if int(self.frame) == 9:
				self.setCurrentAction(0)
		elif self.currentAction == Actions.DIE:
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
			if int(self.frame) == 9:
				self.setCurrentAction(0)

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
		self.displayText(screen, self.name, self.x+16, self.y-16)

