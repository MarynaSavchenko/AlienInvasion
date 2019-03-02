import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    """initialize, create screen, ship and group of bullets"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(screen, ai_settings)
    bullets = Group()

    #Main loop
    while True:

        #Watch for events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        update_bullets(bullets)
        #Update screen
        gf.update_screen(ai_settings, screen, ship, bullets)


def update_bullets(bullets):
    """update bullets and get rid from old one"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


if __name__ == "__main__":
    run_game()