import pygame.font

class Button:
    """Button to start the game."""

    def __init__(self, game, msg):
        """Initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0,150,0)
        self.text_color = (255,255,255)
        self.text = pygame.font.SysFont(None, 36)

        # building and centering button rect obj
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # message only needs to be prepared once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into a rendered image and center it."""

        self.msg_img = self.text.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw img text on the button."""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
        