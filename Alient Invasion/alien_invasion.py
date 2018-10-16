import pygame
from pygame.sprite import Group

import game_functions as gf
from background import Background
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from sound import Sound


# TODO Create saving best records to file class, change static saving
def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    sound = Sound(pygame.mixer)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    background = Background(screen, 'background.jpg', [0, 0])
    pygame.display.set_caption("Alient invasion")

    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, sound)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets, sound)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, background)


run_game()
