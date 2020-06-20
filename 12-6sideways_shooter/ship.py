import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#Start each new ship at the bottom center of the screen.
		self.rect.center = self.screen_rect.midleft

		self.y = float(self.rect.y)

		self.moving_bottom = False
		self.moving_top = False

	def update(self):
		"""Update the ship's position based on the movement flag."""

		if  self.moving_top and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed


		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)