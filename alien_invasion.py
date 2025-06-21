import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class Game:
    """Function for managing the whole game."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Main game loop"""

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Handles events."""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.KEYDOWN):
                self.check_keydown_events(event)
            elif (event.type == pygame.KEYUP):
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = True
        if (event.key == pygame.K_LEFT):
            self.ship.moving_left = True 
        if (event.key == pygame.K_SPACE):
            self._fire_bullet()
        if (event.key == pygame.K_q):
            sys.exit()
        
    def check_keyup_events(self, event):
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = False
        if (event.key == pygame.K_LEFT):
            self.ship.moving_left = False 
            
    def _update_screen(self):
        """Updates the screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_bullets(self):
        # deleting the bullets that have disappeared form the screen
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0):
                self.bullets.remove(bullet)

if __name__ == '__main__':
    ai = Game()
    ai.run_game()
