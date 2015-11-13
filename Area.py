# Area.py: This is meant to be an area of the game
# NOTE: this is in the process of being modified from another game
# Author: Chad Carey, Preston Price

import display
import os.path
import pygame

class Area(display.Renderable):
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

		# define the starting connections
		self._north = None
		self._east = None
		self._south = None
		self._west = None
		self._entranceDescription = "you see another room."

	def setAdjacentAreas(self, n, s, e, w):
		self._north = n
		self._south = s
		self._east = e
		self._west = w

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

	def printOptions(self):
		if self._north != None:
			print "To the north ", self._north.entranceDescription
		if self._south != None:
			print "To the south ", self._south.entranceDescription
		if self._east != None:
			print "To the east ", self._east.entranceDescription
		if self._west != None:
			print "To the west ", self._west.entranceDescription

def main_map():
	m = Area(
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
