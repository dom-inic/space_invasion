# settings file for settings in the game
import pygame
class Settings():
	""" a class to store all settings for alien invasion"""

	def __init__(self):
		"""initialize the game's static settings."""
		# screen setting 
		self.screen_width=1200
		self.screen_height=600
		self.bg_color= (0, 0 , 0)
		# self.bg_image = pygame.image.load('images/background.bmp')
		# self.bg_image('spacex.bmp') trying to add  a background image for the games background.
		
		# ship settings 
		# self.ship_speed_factor = 2
		self.ship_limit = 1
		# bullet settings 
		# self.bullet_speed_factor = 3
		self.bullet_width = 4
		self.bullet_height = 8
		self.bullet_color =255, 0, 102
		self.bullets_allowed = 5

		# startrel settings
		# self.startrek_speed_factor = 3
		self.fleet_drop_speed = 10
		# fleet direction of i represents right; -1 represents left
		# self.fleet_direction = 1

		# how quickly the game speeds up
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""" Initialize settinmgs that change throughout the game """
		self.ship_speed_factor = 1
		self.bullet_speed_factor = 3
		self.startrek_speed_factor = 1.5

		self.fleet_direction = 1

	def increase_speed(self):
		""" increase speed settings """
		self. ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.startrek_speed_factor *= self.speedup_scale

