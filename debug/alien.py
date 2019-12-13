import sys
import pygame 
def run_game():
	pygame.init()
	screen= pygame.display.set_mode((500,500))
	pygame.display.set_caption(" alien inavasion")

	while True:
		for event in pygame.event.get():
			if event.type ===pyagme