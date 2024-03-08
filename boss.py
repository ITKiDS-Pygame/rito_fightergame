import pygame, player, lifebar, bullet, screen

from enum import Enum

class BossMoveState(Enum):
    DOWN = 0
    LEFT = 1
    RIGHT = 2

class Boss:
    def __init__(self, posX, posY):
        self.surface = screen.SURFACE
        self.color = screen.WHITE
        self.speed = 2
        self.health = 100
        self.rect = pygame.Rect(posX, posY, 200, 100)
        self.bullet_list = []
        self.fire_counter = 1
        self.fire_rate = 60
        self.moveState = BossMoveState.DOWN

    def fire(self):
        self.bullet_list.append(bullet.Bullet(self.rect.x, self.rect.y + self.rect.height, fired_by="enemy"))
        self.bullet_list.append(bullet.Bullet(self.rect.x + self.rect.width, self.rect.y + self.rect.height, fired_by="enemy"))

    def move(self, direction):
        if direction == "down":
            self.rect.y += self.speed
        if direction == "left":
            self.rect.x -= self.speed
        if direction == "right":
            self.rect.x += self.speed

    def update(self):
        self.fire_counter += 1
        if self.moveState == BossMoveState.DOWN:
            self.move("down")
            if self.rect.y >= 0:
                self.moveState = BossMoveState.LEFT
        if self.moveState == BossMoveState.RIGHT:
            self.move("right")
            if self.rect.x >= 600:
                self.moveState = BossMoveState.LEFT
        if self.moveState == BossMoveState.LEFT:
            self.move("left")
            if self.rect.x <= 0:
                self.moveState = BossMoveState.RIGHT

        if self.health <= 90 and self.health >= 71:
            self.fire_rate = 40
        elif self.health <= 70 and self.health >= 51:
            self.fire_rate = 30
        elif self.fire_rate <= 50 and self.health >= 31:
            self.fire_rate = 20

        if self.fire_counter % self.fire_rate == 0:
            self.fire()

        for bull in self.bullet_list:
            bull.update()
            if bull.rect.y >= 800:
                self.bullet_list.remove(bull)

    def draw(self):
        for bull in self.bullet_list:
            bull.draw()

        pygame.draw.rect(self.surface, screen.COLORBOSS, self.rect)
