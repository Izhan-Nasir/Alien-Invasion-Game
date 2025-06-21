import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to create and manage bullets"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # all bullet will be drawn at (0,0) initially
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        #bullet initial position as a float for fine adjustment
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)