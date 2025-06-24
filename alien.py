import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to create, handle, and delete aliens."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        """Move alien to the right"""
        self.x += self.settings.alien_speed * self.settings.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        """Returns true if alien is at the edge of the screen otherwise returns
         false """
        screen_rect = self.screen.get_rect()
        return ((self.rect.right >= screen_rect.right) or (self.rect.left <= 0))

