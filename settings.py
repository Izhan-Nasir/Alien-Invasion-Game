class Settings:
    """A class to keep track of all the game settings."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_speed = 10
        self.ships_limit = 3

        # bullet settings
        self.bullet_speed = 5
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (60,60,60)

        # alien settings
        self.alien_speed = 0.5
        self.drop_speed = 2

        # 1 for right and -1 for left
        self.alien_direction = 1

