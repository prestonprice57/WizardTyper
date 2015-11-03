import display
import os
import pygame

# stats class contains entity stats like hp and resistances
class Stats(object):

	def __init__(self):
		self.hp = 100
		self._magicPower = 1.0 # percentage
		self._fireResistance = 1.0 # percentage

	# add properties for magicPower and fireResistance


# Entity is the base class for all game entities. (player, crature...)
class Entity(display.Renderable):

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

	def render(self, screen):
		''' Override in children'''
		pass

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

class Cleric(Entity):
	''' Cleric character'''

#!!! Really, there should be a Mobile object that
#!!! this inherits from.  The Mobile object would
#!!! handle movement.  This would set the movement
#!!! speed and deal with the rendering details.

	# This is essentially a static class variable
	# It contains the mapping of frames in the
	# minotaur sprite map.
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
			display.get_image(
				os.path.join(
					'resources',
					'cleric spritesheet calciumtrice.png'
				)
			)
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 10

		screen.blit(
		    pygame.transform.scale(
		        self.sprite_map.subsurface(
		            pygame.Rect(
		                self.frames[Actions.WALK][int(self.frame)],
		                (32, 32)
		            ),
		        ),
		        (64, 64)
		    ),
		    (self.x, self.y)
		)

class Map(display.Renderable):
	''' Map class

	   Tracks the map data
	'''

	def __init__(self, size, sprite_map, offset=(0,0)):
		''' Constructor

		size -- the width and height of the map as a tuple
		sprite_map -- a Pygame Surface object containing
		              the sprite graphics for map tiles
		offset -- the position of the upper left corner
		          as a tuple, for rendering
		'''
		super(type(self), self).__init__(sprite_map, -1)
		self._map = [0 for i in range(size[0] * size[1])]
		self.size = size
		self.offset = offset

	def render(self, screen):
		for n, tile in enumerate(self._map):
			x = (n % self.size[0]) * 32 + self.offset[0]
			y = (n / self.size[0]) * 32 + self.offset[1]
			tx = (tile % 30) * 16
			ty = (tile / 30) * 16

			screen.blit(
				pygame.transform.scale(
					self.sprite_map.subsurface(
						pygame.Rect(tx, ty, 16, 16)
					),
					(32, 32)
				),
				(x, y),
			)

	def __getitem__(self, (x, y)):
		try:
			return self._map[x + y * self.size[0]]
		except IndexError as e:
			e.args = ("Map index out of range",)
			e.message = "Map index out of range"
			raise

	def __setitem__(self, (x, y), value):
		try:
			self._map[x + y * self.size[0]] = value
		except IndexError as e:
			e.args = ("Map index out of range",)
			e.message = "Map index out of range"
			raise

	def set_map(self, map):
		''' Set the map to a given list

		map -- This is a list of ints mapping to the
		       sprite image.  It must be a list that
		       is exactly the same length as self._map.
		'''

		if type(map) is not list:
			raise Exception("argument is not a list")

		if len(map) == len(self._map):
			self._map = map
		else:
			raise Exception("Map size does not match list size")

def main_map():
	m = Map(
		(16, 16),
	        display.get_image(
			os.path.join(
				'resources',
				'dungeon tileset calciumtrice.png'
			)
		),
		offset=(0, 0)
	)

	tiles = [
		122, 124, 122, 121, 123, 124, 123, 330, 331,124, 123, 123, 123, 124, 123, 153,
		152, 154, 152, 151, 153, 154, 153, 360, 361,154, 153, 153, 153, 154,153, 153,
		44, 211, 219, 220, 220, 218, 219, 218, 220,219, 218, 220, 218, 219,212, 35,
		44, 216, 271, 273, 271, 271, 272, 278, 271,271, 272, 271, 271, 271,226, 35,
		46, 216, 271, 273, 271, 271, 272, 278, 271,271, 272, 271, 271, 271,226, 35,
		44, 217, 272, 274, 272, 274, 273, 272, 271,271, 272, 271, 271, 271,224, 35,
		46, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 35,
		330, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 331,
		360, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 361,
		46, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 35,
		46, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 35,
		46, 215, 271, 271, 272, 271, 271, 271, 271,271, 272, 271, 271, 271,226, 35,
		45, 216, 271, 271, 274, 273, 271, 271, 271,271, 271, 273, 272, 274, 225, 35,
		45, 213, 221, 222, 223, 221, 222, 223, 223,221, 222, 223, 222, 222, 214, 35,
		123, 124, 122, 121, 122, 124, 123, 330, 331,124, 124, 123, 123, 124, 124, 123,
		153, 154, 152, 151, 152, 154, 153, 360, 361,154, 154, 153, 153, 154, 154, 153,
	]

	test_tiles = []
	for i in range(300):
		test_tiles.append(i)

	m.set_map(tiles)
	return m
