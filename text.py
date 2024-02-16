import pygame, screen


class Text:

    def __init__(self, text):
        self.FONT = pygame.font.Font(None, 55)
        self.text = self.FONT.render(text, True, screen.WHITE)
        self.SURFACE = screen.SURFACE

    def draw(self):
        self.SURFACE.blit(self.text, (screen.SCREEN_X / 2, screen.SCREEN_X / 2))