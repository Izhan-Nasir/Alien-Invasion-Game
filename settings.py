class Settings:
    """A class to keep track of all the game settings."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)
        self.ship_speed = 15.5

        # bullet settings
        self.bullet_speed = 7.5
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (60,60,60)
