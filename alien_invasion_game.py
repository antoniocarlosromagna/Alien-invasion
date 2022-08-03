import pygame 
import sys
from settings import Settings 
from ship import Ship
from bullet import Bullet 
from alien import Alien 

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.x_px, self.settings.y_px)) # screen resolution 
        pygame.display.set_caption('Alien invasion') # window name 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        # watch for keybords and mouse events 
        while True:
            self._check_events() 
            self.ship.update()
            self._update_bullets()
            self.bullets.update()
            self._update_aliens()
            self._update_screen()

    def _update_aliens(self):
        # update the position of all aliens in the fleet 
        self.aliens.update()    

    def _update_aliens(self):
        # check if the fleet is at an edge, 
        # then update the position of all aliens in the fleet 

        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship collisions 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")

    def _create_fleet(self):
        # create an alien and find the number of aliens in a row 
        # spacing between each alien is equal to one alien widht 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        alien_width = alien.rect.width
        avaible_space_x = self.settings.x_px - (2 * alien_width)
        number_aliens_x = avaible_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height 
        available_space_y = (
            self.settings.y_px - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # create an alien and place it in the row 
        alien = Alien(self)
        alien_width, alien_heigth = alien.rect.size 
        alien.x = alien_width + 2.7 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_heigth + 2 * alien.rect.height * row_number 
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # resond appropriately if any aliens have reached an edge 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        # drop the entire fleet and change the fleet's direction 
        for alien in self.aliens.sprites(): 
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1 

    def _update_bullets(self):
        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # respond to bullet-alien collisions
        # remove any bullets and aliens that have collided 
        collisions = pygame.sprite.groupcollide(   
            self.bullets, self.aliens, True, True
            )

        if not self.aliens:
            # destroy existing bullets and create new fleet 
            self.bullets.empty()
            self._create_fleet()

    def _check_events(self):
        # respond to keypresses and mouse events
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # respond to keypresses 
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()

    def _check_keyup_events(self, event): 
        # respond to key releases 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        # crate a new bullet and add it to the bullets grup
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # fill the screen
        self.screen.blit(self.settings.img, (0, 0))
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()
        pygame.display.flip() # make the most recently drawn screen visable
      
if __name__ == '__main__':
    # make a game instance, and run the game 
    ai = AlienInvasion()
    ai.run_game()