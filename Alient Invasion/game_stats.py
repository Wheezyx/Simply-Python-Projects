class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = 0
        self.game_active = False
        self.reset_stats()
        self.score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
