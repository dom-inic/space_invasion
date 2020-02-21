# main file for running the game.
import sys
import pygame
# A Group class to help group the bullets
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from ufo import Ufo
import game_functions as gf

def run_game():
	# initialize game and create a screen object.
	pygame.init()
	# make an instance of the class Settings 
	ai_settings= Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("space invasion")
	# make a ship
	ship = Ship(ai_settings, screen)
	# make a group to store the bullets in 
	# bullets an instance of the class Group. created outside the loop to avoid repetition
	bullets = Group()
	# make a group of ufos 
	startreks = Group()

	# create the fleet of startreks
	gf.create_fleet(ai_settings, screen, ship, startreks)
	# make an instance of a ufo
	startrek= Ufo(ai_settings, screen)
	# start the mainloop for the game.

	class Backround(pygame.sprite.Sprite):
		"""a Background class for the background image of the game"""
		def __init__(self, image_file, location):
			# call the sprite initializer
			pygame.sprite.Sprite.__init__(self) 
			self.image = pygame.image.load(image_file)
			self.rect = self.image.get_rect()
			self.rect.left, self.rect.top = location

	background = Backround('images/background.bmp', [0,0])

	screen.fill([255, 255, 255])
	screen.blit(background.image, background.rect)
			
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.key == pygame.K_RIGHT:
					ship.moving_right = True

				if event.key == pygame.K_LEFT:
					ship.moving_left = True
				if event.key == pygame.K_SPACE:
					gf.fire_bullet(ai_settings, screen, ship, bullets)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False

				if event.key == pygame.K_LEFT:
					ship.moving_left = False

		# keyboard and mouse events
		# gf.check_events(ai_settings ,screen,ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, startreks, bullets)
		gf.update_startreks(ai_settings, startreks)

		gf.update_screen(ai_settings,screen,ship, startreks, bullets)
	


run_game()



