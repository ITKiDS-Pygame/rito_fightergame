import pygame, screen, player, enemy, lifebar

class collision_manage:
    def __init__(self, Health, Player, Enemy):
        self.health = Health
        self.player = Player
        self.enemy = Enemy

    def update(self):
        self.collision_player()
    def collision_player(self):
        for bullet in self.enemy.bullet_list:
            if bullet.rect.colliderect(self.player.rect):
                self.health.take_damage(damage=5)
                self.enemy.bullet_list.remove(bullet)


