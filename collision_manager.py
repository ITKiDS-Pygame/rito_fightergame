import pygame, screen, player, enemy, lifebar, random

class collision_manage:
    def __init__(self, Health, Player, Enemy, Boss):
        self.health = Health
        self.player = Player
        self.enemy = Enemy
        self.boss = Boss
        self.enemy_counter = 0
    def update(self):
        self.collision_player()
    def collision_player(self):

        for bullet in self.player.bullet_list:
            if self.enemy.rect.colliderect(bullet):
                self.player.bullet_list.remove(bullet)
                self.enemy_counter += 1
                print(self.enemy_counter)
                self.enemy.rect.x = random.randrange(0, screen.SCREEN_X - self.enemy.size)
                self.enemy.rect.y = -50

        for bullet in self.player.bullet_list:
            if self.boss.rect.colliderect(bullet):
                self.boss.health -= 20
                if self.boss.health <= 0:
                    self.boss.dead = True
                self.player.bullet_list.remove(bullet)

        for bullet in self.enemy.bullet_list:
            if bullet.rect.colliderect(self.player.rect):
                self.health.take_damage(damage=5)
                self.enemy.bullet_list.remove(bullet)

        for bullet in self.boss.bullet_list:
            if bullet.rect.colliderect(self.player.rect):
                self.health.take_damage(damage=10)
                self.boss.bullet_list.remove(bullet)
