import pygame
import sys

def check_events():
    # Watch for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Change display
    pygame.display.flip()