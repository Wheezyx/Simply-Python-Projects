import pygame


class Background:

    def __init__(self, screen,  file, location):
        self.screen = screen
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def blitme(self):
        self.screen.blit(self.image, self.rect)
