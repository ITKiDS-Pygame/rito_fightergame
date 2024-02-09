import pygame, screen, bullet

class Player:
    def __init__(self, startX, startY):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.width = 50
        self.height = 20
        self.speed = 5
        self.bullet_list = []
        self.rect = pygame.Rect(startX, startY, self.width, self.height)
        self.cooldown = 0

    def move(self, dir):
        if dir == "left":
            self.rect.x -= self.speed
        if dir == "right":
            self.rect.x += self.speed

    def fire(self):
        if len(self.bullet_list) < 4:
            self.bullet_list.append(bullet.Bullet(self.rect.x + self.width / 2, self.rect.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move("right")
        if keys[pygame.K_LEFT]:
            self.move("left")
        if keys[pygame.K_SPACE]:
            if self.cooldown % 100 == 0 or self.cooldown == 0:
                self.fire()
            self.cooldown += 5
        else:
            self.cooldown = 0

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= screen.SCREEN_X - self.width:
            self.rect.x = screen.SCREEN_X - self.width

        for bullet in self.bullet_list:
            bullet.update()
            for bullet in self.bullet_list:
                bullet.update()
                if bullet.rect.y <= -bullet.size:
                    self.bullet_list.remove(bullet)

    def draw(self):
        for bullet in self.bullet_list:
            bullet.draw()
        pygame.draw.rect(self.surface, self.color, self.rect)
