import pygame, collision_manager, random, screen, player, enemy, lifebar

player = player.Player(screen.SCREEN_X / 2, screen.SCREEN_Y - 60)
enemy = enemy.Enemy(random.randrange(0, screen.SCREEN_X - 50), -50)
health = lifebar.Health(screen.SCREEN_X - 150, 50)
collision_manage = collision_manager.collision_manage(health, player, enemy)

def draw():
    player.draw()
    enemy.draw()
    health.draw()

def update():
    screen.CLOCK.tick(screen.FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit(1)

    for bullet in player.bullet_list:
        if enemy.rect.colliderect(bullet):
            player.bullet_list.remove(bullet)
            enemy.rect.x = random.randrange(0, screen.SCREEN_X - enemy.size)
            enemy.rect.y = -50

    draw()
    enemy.update()
    player.update()
    collision_manage.update()
    pygame.display.update()
    screen.SURFACE.fill(screen.BLACK)

def run():
    while True:
        update()

if __name__ == '__main__':
    run()
