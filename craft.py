# main file for running the game.
import sys
import pygame
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
	# bg_color=(255, 255, 255)
	# start the mainloop for the game.
	while True:

		# keyboard and mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)


run_game()



