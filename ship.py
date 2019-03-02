import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        #Load image, gets rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Start ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal
        self.center = float(self.rect.centerx)

        self.moving_rigth = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move contionious"""
        if self.moving_rigth and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.speed_factor

        self.rect.centerx = self.center

