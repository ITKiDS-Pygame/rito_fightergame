import pygame
import screen

class Player:
    def __init__(self, startX, startY):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.width = 50
        self.height = 20
        self.speed = 5
        self.rect = pygame.Rect(startX, startY, self.width, self.height)

    def move(self, dir):
        if dir == "left":
            self.rect.x -= self.speed
        if dir == "right":
            self.rect.x += self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move("right")
        if keys[pygame.K_LEFT]:
            self.move("left")

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= screen.SCREEN_X - self.width:
            self.rect.x = screen.SCREEN_X - self.width

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)