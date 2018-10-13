class Sound:
    def __init__(self, mixer):
        self.shoot_sound = mixer.Sound('laser1.wav')
        self.killed_sound = mixer.Sound('invaderkilled.wav')
        self.level_up_sound = mixer.Sound('level_up.wav')
        self.lose_ship_sound = mixer.Sound('lose_ship.wav')
