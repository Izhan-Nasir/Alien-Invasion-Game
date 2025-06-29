import pygame.font
from ship import Ship
from pygame.sprite import Group 


class Scoreboard:
    """A class to report scoring information to the user."""

    def __init__(self, game):
        """Initialize score-keeping attributes."""

        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # text settings
        self.text_font = pygame.font.SysFont(None, 28)
        self.text_color = (30,30,30)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Render the score as an image."""

        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_img = self.text_font.render(score_str, True, self.text_color
                                               , self.settings.bg_color)
        
        # position the rendered image
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        """Display scores, level and ship lives on the screen."""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_img_rect)
        self.screen.blit(self.level_img, self.level_img_rect)
        self.ships.draw(self.screen)

    def prep_highscore(self):
        """Render highscore as an image."""

        rounded_highscore = round(self.stats.highscore)
        highscore_str = f"Highscore: {rounded_highscore:,}"
        self.highscore_img = self.text_font.render(
            highscore_str, True, self.text_color, self.settings.bg_color)
        
        self.highscore_img_rect = self.highscore_img.get_rect()
        self.highscore_img_rect.top = self.screen_rect.top + 20
        self.highscore_img_rect.centerx = self.screen_rect.centerx

    def _check_highscore(self):
        """Check if there is a new highscore."""

        if (self.stats.score > self.stats.highscore):
            self.stats.highscore = self.stats.score
            self.prep_highscore()

    def prep_level(self):
        """Render level as img on screen."""

        level_text = f"Level: {self.stats.level}"
        self.level_img = self.text_font.render(level_text,
                                               True, self.text_color, 
                                               self.settings.bg_color)
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.top = self.screen_rect.top + 36 + 12
        self.level_img_rect.right = self.screen_rect.right - 20
     
    def increase_level(self):
        """Increment level and re-render the text image."""
        self.stats.level += 1
        self.prep_level()

    def prep_ships(self):
        """Render ship images which represent player's lives."""

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
