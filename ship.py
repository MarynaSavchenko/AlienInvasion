import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        #Load image, gets rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Start ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
