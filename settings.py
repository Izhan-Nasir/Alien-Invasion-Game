class Settings:
    """A class to keep track of all the game settings."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)

        # ship settings
        self.ships_limit = 3

        # bullet settings
        self.bullet_color = (60,60,60)

        # alien settings
        self.drop_speed = 2

        # 1 for right and -1 for left
        self.alien_direction = 1

        # speed speeding-up factor
        self.speedup_factor = 1.2

        # score scaling factor
        self.score_scaling = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings of the game."""

        self.ship_speed = 3.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 10
        self.alien_points = 10

    def increase_speed(self):
        """Increase the game speed."""

        self.ship_speed *= (self.speedup_factor - 0.1)
        self.bullet_speed *= (self.speedup_factor - 0.1)
        self.alien_speed *= self.speedup_factor
        self.bullet_width *= (self.speedup_factor)
        self.bullet_height *= (self.speedup_factor - 0.12)

        # scoring
        self.alien_points = int(self.alien_points * self.score_scaling)

