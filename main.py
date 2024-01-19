import pygame
import random
import screen
import player
import enemy

player = player.Player(screen.SCREEN_X / 2, screen.SCREEN_Y - 60)
enemy = enemy.Enemy(random.randrange(0, screen.SCREEN_X - 50), -50)

def draw():
    player.draw()
    enemy.draw()

def update():

    screen.CLOCK.tick(screen.FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit(1)

    draw()

    enemy.update()
    player.update()
    pygame.display.update()
    screen.SURFACE.fill(screen.BLACK)

def run():
    while True:
        update()

if __name__ == '__main__':
    run()