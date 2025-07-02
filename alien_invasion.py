import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class Game:
    """Manage the whole game."""

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()  # objects for keeping track of game settings
        self.screen = pygame.display.set_mode((1200, 720))
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)  # object for ship management
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self) # object for handling game stats
        self.game_active = False # starting 
        self.play_button = Button(self,"Play")
        self.scoreboard = Scoreboard(self)

        self.high_score_music_triggered = False # <--- ADD THIS LINE


        # helper method
        self._create_fleet()

        # sounds effects
        self.shoot_sound = pygame.mixer.Sound("Sound/Shoot.wav")
        self.shoot_sound.set_volume(0.2)
        self.alien_kill_sound = pygame.mixer.Sound("Sound/Alien_Destroy.wav")
        self.alien_kill_sound.set_volume(0.4)
        self.lose_sound = pygame.mixer.Sound("Sound/Lose.wav")
        self.level_up_sound = pygame.mixer.Sound("Sound/Level_up.wav")

        # Background music
        self.music_playlist = [
            "Sound/Background_1.mp3",
            "Sound/Background_2.mp3",
            "Sound/Oppenheimer.mp3",
            "Sound/Trinity.mp3"
        ]

        self.music_index = -1

        # defining a custom event for when music finishes
        self.MUSIC_END_EVENT = pygame.USEREVENT + 1

    def run_game(self):
        """Main game loop"""

        if (not self.game_active):
            self.play_menu_music() # automatically turns off when play is pressed
        while True:
            self._check_events()
            if (self.game_active):
                self.update_bullets()
                self._update_aliens()
                self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Handles events."""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.stats.save_highscore() # saving highscore before closing
                sys.exit()
            elif (event.type == self.MUSIC_END_EVENT):
                self._play_next_song()
            elif (event.type == pygame.KEYDOWN):
                self.check_keydown_events(event)
            elif (event.type == pygame.KEYUP):
                self.check_keyup_events(event)
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def check_keydown_events(self, event):
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = True
        if (event.key == pygame.K_LEFT):
            self.ship.moving_left = True 
        if (event.key == pygame.K_SPACE):
            self._fire_bullet()
        if (event.key == pygame.K_q):
            self.stats.save_highscore() # saving highscore before closing
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
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        if not (self.game_active):
            self.play_button.draw_button()
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        self.shoot_sound.play()
   
    def update_bullets(self):
        self.bullets.update()
        # deleting the bullets that have disappeared form the screen
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0):
                self.bullets.remove(bullet)
        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        """Detect bullet and alien collisions and delete both."""

        # collisions dictionary is used for storing scores
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)

        if not (self.aliens):
            # delete existing bullets and create a new fleet if all aliens 
            # are dead
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed() # increase speed for new level
            self.scoreboard.increase_level()
            self.level_up_sound.play() 

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.scoreboard._check_highscore()
                self.scoreboard.prep_score() # recreate the score img 
                self.alien_kill_sound.play()

    def _create_fleet(self):
        """Draws a fleet of ships"""
        alien = Alien(self)

        # Keep on creating aliens until no space is left
        # Space between two aliens is one alien-width and space between 
        # two alien rows is one alien-height

        alien_width , alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height + 20
        current_x += 20

        while ((current_y < (self.settings.screen_height - 6 * alien_height))):
            while ((current_x < (self.settings.screen_width - 2 * alien_width))):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # resetting the value of x for new row and incrementing y
            current_x = 20 + alien_width
            current_y += 2 * alien_height

    def _create_alien(self, position_x, position_y):
        """Create alien and add it to the sprite group"""
        new_alien = Alien(self)
        new_alien.x = position_x # this is our custom attribute used for 
                                 # adjustments of horizontal positioning 
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond to fleet colliding with the edge."""
        for alien in self.aliens.sprites():
            if (alien.check_edges()):
                self._change_direction()
                break
        
    def _change_direction(self):
        """Move the entire fleet down and reverse the direction of the fleet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_speed   
            
        self.settings.alien_direction *= -1
 
    def _update_aliens(self):
        """Check if an alien is at the edge and update its position"""
        self._check_fleet_edges()
        self.aliens.update()

        # detect ship-alien collision
        if (pygame.sprite.spritecollideany(self.ship, self.aliens)):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship and alien collision."""
        
        self.lose_sound.play()
        if (self.stats.ships_left > 0):
            self.stats.ships_left -= 1 # decrement the ship lives
            self.scoreboard.prep_ships()

            # delete the old stuff
            self.bullets.empty()
            self.aliens.empty()

            # Create new fleet and center the ship 
            self._create_fleet()
            self.ship.center_ship()

            sleep(2) # pause for 0.5 second
        else:
            self.game_active = False
            pygame.mouse.set_visible(True) # making the cursor visible

    def _check_aliens_bottom(self):
        """Respond appropriately if an alien has reached the bottom"""
        for alien in self.aliens.sprites():
            if (alien.rect.bottom >= self.settings.screen_height):
                # same as collision between aliens and ship
                self._ship_hit()
                break

    def _check_play_button(self, mos):
        """Start a new game when player clicks on play button."""
        
        button_clicked = self.play_button.rect.collidepoint(mos)
        if ((button_clicked) and (not self.game_active)):
            self._play_next_song()
            self.stats.reset_stats()
            self.scoreboard.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self.game_active = True 
            self.ship.center_ship()
            self._create_fleet()
            self.settings.initialize_dynamic_settings()
            self.scoreboard.prep_score() # score resets to zero to start fresh 
            
            # hiding the cursor
            pygame.mouse.set_visible(False)

    def play_menu_music(self):
        """Play menu background music."""
            
        pygame.mixer.music.load("Sound/Menu_Sound.mp3")
        pygame.mixer.music.play(-1)

    def _play_next_song(self):
        """Play the next song in the playlist."""

        self.music_index = (self.music_index + 1) % len(self.music_playlist)

        pygame.mixer.music.load(self.music_playlist[self.music_index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)


if __name__ == '__main__':
    ai = Game()
    ai.run_game()
