import pygame

class Ship:
    """A class to handle the ship."""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = game.settings
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the ship."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        if ((self.moving_right) and (self.rect.right < self.screen_rect.right)):
            self.x += self.settings.ship_speed
        if ((self.moving_left) and (self.rect.left > 0)):
            self.x -= self.settings.ship_speed

        self.rect.x = self.x