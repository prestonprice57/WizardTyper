import Display
import os
import pygame

class Actions(object):
	''' Action state enum'''
	ACTIVE = 0
	INACTIVE = 1


# Entity is the base class for all game entities. (player, crature...)
class SpellAnimation(Display.Renderable):

	def __init__(self, sprite_map, name):
		# Call the parent constructor
		super(SpellAnimation, self).__init__(sprite_map, 10)
		self.tile = (0, 0)	# Location in tile units as float
		self.x = 4
		self.y = 4

	def render(self, screen):
		''' Override in children'''
		pass

	def setCurrentAction(self, actionNum):
		''' override in children '''
		pass

	def updateAnimation(self,entity):
		pass


class FireAnimation(SpellAnimation):
	fireballList = []

	for i in range(4):
		y = i*64
		for j in range(4):
			x = j*64
			fireballList.append((x,y))

	print fireballList
	frames = {
		Actions.ACTIVE   : fireballList,
		Actions.INACTIVE : 0
	}

	def __init__(self):
		super(FireAnimation, self).__init__(
			Display.get_image(
				os.path.join(
					'resources',
					'exp2_0.png'
				)
			),
			None
		)
		self.clock = pygame.time.Clock()
		self.frame = 0.0
		self.currentAction = Actions.ACTIVE
		self.x = 550
		self.y = 225
		self.animationCompleted = False
		self.effectApplied = False

	def updateAnimation(self, entity):
		self.x = entity.x
		self.y = entity.y
		self.effectApplied = entity.effectApplied
		

	def render(self, screen):

		# Convert tile/subtile to screen coordinates
		#x = int(self.tile[0] * 32)
		#y = int(self.tile[1] * 32)

		self.frame = (self.frame + (self.clock.tick() / 100.0)) % 12

		"""if self.currentAction == Actions.ACTIVE and not self.animationCompleted:
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
			)"""

		if int(self.frame) == 11:
			self.animationCompleted = True
			self.currentAction = Actions.INACTIVE

		if self.currentAction == Actions.ACTIVE:# and self.effectApplied == True:
			self.frame = (self.frame + (self.clock.tick() / 100.0)) % 5 + 6
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
			    (self.x, self.y+10)
			)


	def setCurrentAction(self, actionNum):
		if actionNum == 0:
			self.currentAction = Actions.INACTIVE
		elif actionNum == 1:
			self.currentAction = Actions.ACTIVE
		else:
			print "Invalid input. Current action not changed."
