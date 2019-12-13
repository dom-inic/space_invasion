# game functions file for functions in the game  to reduce the longetivity of the game and make it easy to debug
import sys
import pygame

def check_keydown_events(event,ship):
	"""respond to keypresses """

	if event.key == pygame.K_RIGHT:
		# move the ship to thhe right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# move the ship to the left
		ship.moving_left = True

	elif event.key == pygame.K_ESCAPE:
		sys.exit()
def check_keyup_events(event,ship):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.type == pygame.K_LEFT:
		ship.moving_left = False



def check_events(ship):
	""" respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


				
def update_screen(ai_settings,screen, ship):
	"""update images on the screen and flip to the new screen"""
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# make the most recently drawn screen visible
	pygame. display.flip()



