# main file for running the game.
import sys
import pygame
# A Group class to help group the bullets
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# initialize game and create a screen object.
	pygame.init()
	ai_settings= Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("space invasion")
	# make a ship
	ship = Ship(ai_settings, screen)
	# make a group to store the bullets in 
	# bullets an instance of the class Group. created outside the loop to avoid repetition
	bullets = Group()
	# start the mainloop for the game.
	while True:

		# keyboard and mouse events
		gf.check_events(ai_settings ,screen,ship, bullets)
		ship.update()
		gf.update_bullets(bullets)

		gf.update_screen(ai_settings,screen,ship, bullets)


run_game()



