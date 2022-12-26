class GameStats:
    # track statistics for Alien Invasion 

    def __init__(self, ai_game):
        # initialize statistics 
        self.settings = ai_game.settings
        self.reset_stats()
        
        # start alien invasion in an active state 
        self.game_active = False # starts in an inactive state 

        # high score should never be rest 
        self.high_score = 0 

    def reset_stats(self):
        # initialize statistics that can change during the game 
        self.ships_left = self.settings.ship_limit 
        self.score = 0
        self.level = 1         