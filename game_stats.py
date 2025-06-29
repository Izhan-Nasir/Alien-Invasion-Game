import pygame
from pathlib import Path
import json

class GameStats:
    """Tracks and manage stats of the game."""

    def __init__(self, game):
        self.settings = game.settings
        self.get_highscore()

        self.reset_stats()  # reset the stats every time a new game is started 

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0 # current score of the player
        self.level = 1

    def get_highscore(self):
        """Reads highscore from the saved file on device."""

        File = Path("Highscore.json")
        if (File.exists()):
            highscore = File.read_text()
            highscore = json.loads(highscore)
            self.highscore = highscore
        else:
            self.highscore = 0 # no previous record then highscore is zero
    
    def save_highscore(self):
        """Saves highscore on device."""
        File = Path("Highscore.json")
        file_content = json.dumps(self.highscore)
        File.write_text(file_content)