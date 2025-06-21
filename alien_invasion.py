import sys
import pygame
from settings import Settings
from ship import Ship

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

    def run_game(self):
        """Main game loop"""

        while True:
            self._check_events()
            self.ship.update()
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
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = Game()
    ai.run_game()
