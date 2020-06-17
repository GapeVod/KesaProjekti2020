import pygame

class MyOwnCharacter:
	"""asd"""
	def __init__(self, ai_game):
		"""asd"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ukko.bmp')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
