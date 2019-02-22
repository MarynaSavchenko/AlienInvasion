import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():

    """initialize and screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(screen)

    #Main loop
    while True:

        #Watch for events
        gf.check_events()

        #Update screen
        gf.update_screen(ai_settings, screen, ship)


if __name__ == "__main__":
    run_game()