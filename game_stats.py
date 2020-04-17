import pygame
class Gamestats():
	""" track statistics for out game """

	def __init__(self, ai_settings):
		""" initialize statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		""" initialize statistics that can change during the game"""
		self.ships_left = self.ai_settings.ship_limit

class Gameover():
	""" a class to show game over when the player has ran out of ships"""

	def __init__(self, screen):
		"""initialize gameover and set its starting position"""
		self.screen = screen

		# load the skeleton image and get its rect.
		self.image = pygame.image.load('images/gameover.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each new skeleton at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		""" draw game over at its current location """
		self.screen.blit(self.image, self.rect)