import pygame
import Entities
import area

pygame.display.init()
screen = pygame.display.set_mode((1024,768))

pygame.display.flip()
wizard = pygame.image.load('resources/cleric spritesheet calciumtrice.png')
screen.blit(wizard,(50,100))

area.register(Entities.main_map())

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	area.render()

	pygame.display.flip()