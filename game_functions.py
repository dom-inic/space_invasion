# game functions file for functions in the game  to reduce the longetivity of the game and make it easy to debug
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings, screen,ship, bullets):
	"""respond to keypresses """

	if event.key == pygame.K_RIGHT:
		# move the ship to thhe right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# move the ship to the left
		ship.moving_left = True

	elif event.key == pygame.K_ESCAPE:
		sys.exit()
	elif  event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		

def fire_bullet(ai_settings, screen, ship, bullets):
	""" fire a bullet if limit not yet reached"""
	# create a new bullet and add it to the bullet's group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet =Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
def check_keyup_events(event,ship):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.type == pygame.K_LEFT:
		ship.moving_left = False



def check_events(ai_settings,screen, ship, bullets):
	""" respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings, screen,ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


				
def update_screen(ai_settings,screen, ship, bullets):
	"""update images on the screen and flip to the new screen"""
	screen.fill(ai_settings.bg_color)
	# redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()

	# make the most recently drawn screen visible
	pygame. display.flip()
def update_bullets(bullets):
	""" update the position of bullets and get rid of old bullets"""
	# update the bullet's position
	bullets.update()

	# a for loop to get rid of bullets that have dissappere to avoid slowing down the game
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)



