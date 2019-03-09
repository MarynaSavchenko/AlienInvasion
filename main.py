import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats



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

    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Main loop
    while True:

        #Watch for events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            #Update ship, bullets, aliens
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings,screen, stats, ship, bullets, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)




if __name__ == "__main__":
    run_game()