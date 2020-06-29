import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game statistcs.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Make the Play button.
        self.play_button = Button(self, "Play")


    def run_game(self):
    	"""Start the mainloop for the game."""
    	while True:
    		self._check_events()

    		if self.stats.game_active:
    			self.ship.update()
    			self._update_bullets()
    			self._update_aliens()
    			
    		self._update_screen()

    def _check_events(self):
    	#Watch for keyboard and mouse events.
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			sys.exit()

    		elif event.type == pygame.MOUSEBUTTONDOWN:
    			mouse_pos = pygame.mouse.get_pos()
    			self._check_play_button(mouse_pos)

    		elif event.type == pygame.KEYDOWN:
    			self._check_keydown_events(event)

    		elif event.type == pygame.KEYUP:
    			self._check_keyup_events(event)


    def _check_keydown_events(self, event):
    	"""Respond to keypresses"""
    	if event.key == pygame.K_RIGHT:
    		self.ship.moving_right = True
    	elif event.key == pygame.K_LEFT:
    		self.ship.moving_left = True
    	elif event.key == pygame.K_UP:
    		self.ship.moving_top = True
    	elif event.key == pygame.K_DOWN:
    		self.ship.moving_bottom = True
    	elif event.key == pygame.K_q:
    		sys.exit()
    	elif event.key == pygame.K_SPACE:
    		self._fire_bullet()
    	elif event.key == pygame.K_p:
    		self._start_game()


    def _check_keyup_events(self, event):
    	"""Respond to key releases"""
    	if event.key == pygame.K_RIGHT:
    		self.ship.moving_right = False
    	elif event.key == pygame.K_LEFT:
    		self.ship.moving_left = False
    	elif event.key == pygame.K_UP:
    		self.ship.moving_top = False
    	elif event.key == pygame.K_DOWN:
    		self.ship.moving_bottom = False

    def _check_play_button(self, mouse_pos):
    	"""Start a new game when the player clicks Play."""
    	button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    	if button_clicked and not self.stats.game_active:
    		self._start_game()

    def _start_game(self):
    	"""Start game."""
    	#Reset the game statistics.
    	self.stats.reset_stats()
    	self.stats.game_active = True

    	#REset the game settings.
    	self.settings.initialize_dynamic_settings()

    	#Get rid of any remaining aliens and bullets.
    	self.aliens.empty()
    	self.bullets.empty()

    	#Create a new fleet and center the ship.
    	self._create_fleet()
    	self.ship.center_ship()

    	#Hide the mouse cursor.
    	pygame.mouse.set_visible(False)

    def _fire_bullet(self):
    	"""Create a new bullet and add it to the bullets group."""
    	if len(self.bullets) < self.settings.bullets_allowed:
    		new_bullet = Bullet(self)
    		self.bullets.add(new_bullet)

    def _update_bullets(self):
    	"""Update position of bullets and get rid of old bullets."""
    	#Update bullet positions.
    	self.bullets.update()

    	#Get rid of bullets that have disappeared.
    	if len(self.bullets) == self.settings.bullets_allowed:
    		self._ship_hit()

    	self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
    	"""Respond to bullet-alien collisions."""
    	#Remove any bullets and alien that have collided.
    	collisions = pygame.sprite.groupcollide(
    		self.bullets, self.aliens, True, True)

    	if not self.aliens:
    		#Destroy existing bulelts and create a new fleet.
    		self.bullets.empty()
    		self._create_fleet()
    		self.settings.increase_speed()

    def _create_fleet(self):
    	"""Create the fleet of aliens."""
    	#Create an alien and find the number of aliens in a row.
    	#Spacing between each alien is equal to one alien width
    	alien = Alien(self)
    	self._create_alien()

    def _create_alien(self):
    	"""Create an alien and place it in the row."""
    	alien = Alien(self)

    	self.aliens.add(alien)

    def _update_aliens(self):
    	"""Update the postitions of all aliens in the fleet."""
    	self._check_fleet_edges()
    	self.aliens.update()

    	#Look for alien-ship collisions.
    	if pygame.sprite.spritecollideany(self.ship, self.aliens):
    		self._ship_hit()

    	#Look for aliens hitting the bottom of the screen.
    	#self._check_aliens_bottom()

    def _check_fleet_edges(self):
    	"""Respond appropriately if any aliens have reaches an edge."""
    	for alien in self.aliens.sprites():
    		if alien.check_edges():
    			self._change_fleet_direction()
    			self.settings.increase_speed()
    			break

    def _change_fleet_direction(self):
    	"""Drop the entire fleet and change the fleet's direction."""
    	for alien in self.aliens.sprites():
    		alien.rect.y += self.settings.fleet_drop_speed
    	self.settings.fleet_direction *= -1

    def _ship_hit(self):
    	"""Respond to the ship being hit by an alien."""
    	if self.stats.ships_left > 0:
    		#Decrement ships-left
    		self.stats.ships_left -= 1

    		#Get rid of any remaining aliens and bullets.
    		self.aliens.empty()
    		self.bullets.empty()

    		#Create a new fleet and center the ship.
    		self._create_fleet()
    		self.ship.center_ship()

    		# Pause.
    		sleep(0.5)
    	else:
    		self.stats.game_active = False
    		pygame.mouse.set_visible(True)


    def _update_screen(self):
    	#Redraw the scren during each pass through the loop.
    	self.screen.fill(self.settings.bg_color)
    	self.ship.blitme()
    	for bullet in self.bullets.sprites():
    		bullet.draw_bullet()
    	self.aliens.draw(self.screen)

    	#Draw the play button if the game is inactive.
    	if not self.stats.game_active:
    		self.play_button.draw_button()

    	# Make the most recently drawn screen visible.
    	pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()