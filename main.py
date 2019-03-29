import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    """initialize, create screen, ship and group of bullets"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship, group of bullets and aliens
    ship = Ship(screen, ai_settings)
    aliens = Group()
    bullets = Group()
    start_button = Button(screen, "Start")
    stats = GameStats(ai_settings)
    sb = Scoreboard(screen, ai_settings, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Main loop
    while True:

        #Watch for events
        gf.check_events(ai_settings, screen, ship, bullets, start_button, stats, aliens, sb)

        if stats.game_active:
            #Update ship, bullets, aliens
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings,screen, stats, ship, bullets, aliens, sb)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, start_button, stats, sb)




if __name__ == "__main__":
    run_game()