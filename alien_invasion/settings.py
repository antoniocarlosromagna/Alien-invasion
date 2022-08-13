from select import select
import pygame 

class Settings: 
    # a class to store all settings for Alien invasion

    def __init__(self):
        # initialize the game's static settings  
        self.x_px = 1280
        self.y_px = 720
        self.bg_color = (23, 24, 39)
        self.img = pygame.image.load('images_ai/back.bmp')

        # ship settings 
        self.ship_speed = 1.3
        self.ship_limit = 3  

        # bullet settings 
        self.bullet_speed = 2.0
        self.bullet_x_px = 3
        self.bullet_y_px = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3 

        # alien settins 
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10 

        # fleet_direction of 1 represents right; -1 represents left 
        self.fleet_direction = 1 

        # how quickly the game speeds up 
        self.speedup_scale = 1.1 

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # initialize settings that change throught the game 
        self.ship_speed = 1.5 
        self.bullet_speed = 3.0 
        self.alien_speed = 1.0 

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1 
    
    def increase_speed(self):
        # increase speed settings 
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        