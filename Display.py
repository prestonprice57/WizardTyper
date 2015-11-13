import pygame

screen = None

# List of registered renderable objects
# that need to be rendered on every frame
renderables = []

# Dictionary of loaded images,
# where the key is the filename
images = {}

class Renderable(object):
	''' Abstract class for renderable objects

	Renderable object should render themselves
	when the render() method is called
	'''

	def __init__(self, sprite_map, z_index=0):
		''' Constructor

		sprite_map -- pygame screen object containing any
		              sprites needed to render this object
		z_index    -- This will be used to sort the renderables
		              list when rendering.  z_index is
		              distance from the "camera."
		'''
		self.sprite_map = sprite_map
		self.z_index = z_index

	def render(self, screen):
		''' Function called by the renderer'''
		pass

	def __lt__(self, other):
		return self.z_index < other.z_index

	def __le__(self, other):
		return self.z_index <= other.z_index

	def __eq__(self, other):
		return self.z_index == other.z_index

	def __ne__(self, other):
		return self.z_index != other.z_index

	def __gt__(self, other):
		return self.z_index > other.z_index

	def __ge__(self, other):
		return self.z_index >= other.z_index

def init(width, height):
	global screen

	if screen:
		raise Exception("A screen has already been initialized")

	screen = pygame.display.set_mode((width, height))

def register(renderable):
	''' Register a renderable object

	renderable -- an object with a render() method
	'''

	renderables.append(renderable)

def render():
	''' Render all registered renderables'''

	global screen

	screen.fill((255, 255, 255))

	# Sort in ascending order, so higher z_index is on top.
	for renderable in sorted(renderables):
		renderable.render(screen)

	pygame.display.flip()

def get_image(filename):
	''' On demand image loader

	filename -- the name of the image file

	If the requested image is already loaded,
	the existing surface is returned
	'''

	global images

	if filename in images:
		return images[filename]
	else:
		image = pygame.image.load(filename)
		image.convert()
		image.convert_alpha()
		images[filename] = image
		return image
