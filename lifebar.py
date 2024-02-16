import pygame, screen, bullet, player, enemy

class Health:
    def __init__(self, posX, posY, game):
        self.surface = screen.SURFACE
        self.damage_color = (255, 0, 0)
        self.life_color = (0, 255, 0)
        self.width = 100
        self.height = 20
        self.damage_rect = pygame.Rect(posX, posY, self.width, self.height)
        self.life_rect = pygame.Rect(posX, posY, self.width, self.height)
        self.game = game

    def take_damage(self, damage=1):
        self.life_rect.width -= damage
        if self.life_rect.width <= 0:
            self.life_rect.width = 0
            self.game.game_over()



    def draw(self):
        pygame.draw.rect(self.surface, self.damage_color, self.damage_rect)
        pygame.draw.rect(self.surface, self.life_color, self.life_rect)
