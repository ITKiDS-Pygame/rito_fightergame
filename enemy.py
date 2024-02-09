import random
import pygame
import bullet
import screen

class Enemy:
    def __init__(self, posX, posY):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.size = 50
        self.speed = 3
        self.rect = pygame.Rect(posX, posY, self.size, self.size)
        self.bullet_list = []


    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= screen.SCREEN_Y:
            self.rect.x = random.randrange(0, screen.SCREEN_X - self.size)

        if len(self.bullet_list) < 1:
            self.bullet_list.append(bullet.Bullet(self.rect.x + (self.rect.width / 2),
                                                  self.rect.y + self.rect.height, fired_by="enemy"))

        for bull in self.bullet_list:
            bull.update()
            if bull.rect.y >= screen.SCREEN_Y:
                self.bullet_list.remove(bull)

    def draw(self):
        for bull in self.bullet_list:
            bull.draw()
        pygame.draw.rect(self.surface, self.color, self.rect)