import pygame

class GameStats:
    """Tracks and manage stats of the game."""

    def __init__(self, game):
        self.settings = game.settings

        self.reset_stats()  # reset the stats every time a new game is started 

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit

    