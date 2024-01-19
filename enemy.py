import random

import pygame
import screen

class Enemy:
    def __init__(self, posX, posY):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.size = 50
        self.speed = 3
        self.rect = pygame.Rect(posX, posY, self.size, self.size)
# comment
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= screen.SCREEN_Y:
            self.rect.x = random.randrange(0, screen.SCREEN_X - self.size)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)