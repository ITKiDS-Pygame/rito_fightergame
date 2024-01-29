import pygame
import screen
import player

class Bullet:
    def __init__(self, startX, startY, fired_by="player"):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.speed = 7
        self.fired_by = fired_by
        self.size = 10
        self.rect = pygame.Rect(startX, startY, self.size, self.size)

    def update(self):
        if self.fired_by == "player":
            self.rect.y -= self.speed

        if self.fired_by == "enemy":
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)