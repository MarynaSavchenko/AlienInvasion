import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move alien to the right"""
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.ai_settings.screen_width:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

    #Unnecessary
    def blitme(self):
        """draw an alien"""
        self.screen.blit(self.image, self.rect)