from time import sleep

import pygame
import sys
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """Watch for events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Check keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Check keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if it is possible. Add bullet to group"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """Update bullets and get rid from old one"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens)
    check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens)


def check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens):
    # Check for collisions and delete aliens
    # Third arg tells to dalete collisioned bullet, fourth - alien
    pygame.sprite.groupcollide(bullets, aliens, False, True)

    # If fleet is empty, create new one
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)



def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Change display
    pygame.display.flip()

def create_fleet(ai_settings, screen, ship, aliens):
    """Creating a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_of_aliens = get_number_of_aliens(ai_settings, alien)
    number_of_rows = get_number_of_rows(ai_settings, ship, alien)

    for row in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(ai_settings, screen, aliens, alien_number, row)

def get_number_of_aliens(ai_settings, alien):
    alien_width = alien.rect.width
    avaible_space_x = ai_settings.screen_width - 2 * alien_width
    return int(avaible_space_x / (2 * alien_width))

def get_number_of_rows(ai_settings, ship, alien):
    alien_height = alien.rect.height
    avaible_space_y = ai_settings.screen_height - 3*alien_height - ship.rect.height
    return int(avaible_space_y/(2*alien_height))



def create_alien(ai_settings, screen, aliens, alien_number, row):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = 2 * alien_number * alien_width + alien_width
    alien.rect.y = alien_height + 2*alien_height*row
    alien.rect.x = alien.x
    aliens.add(alien)

def update_aliens(ai_settings,screen, stats, ship, bullets, aliens):
    """Check if the fleet is on the edge
    and update the position"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,screen, stats, ship, bullets, aliens)

    check_aliens_bottom(ai_settings,screen, stats, ship, bullets, aliens)

def ship_hit(ai_settings,screen, stats, ship, bullets, aliens):
    """Response to ship being hit by a bullet"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        bullets.empty()
        aliens.empty()

        create_fleet(ai_settings,screen, ship, aliens )
        ship.center = ship.screen_rect.centerx
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings,screen, stats, ship, bullets, aliens):
    """Check if any of aliens reaches the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen, stats, ship, bullets, aliens)


def change_fleet_directions(ai_settings, aliens):
    """Drop the entire fleet and change the direction"""
    for alien in aliens:
        alien.rect.y += ai_settings.drop_speed_factor
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break



