import pygame, collision_manager, random, screen, player, enemy, boss, lifebar, text, mixer

pygame.font.init()

#music関係
pygame.mixer.init()
MIXER = mixer.Mixer()

MIXER.music()

class Game():
    def __init__(self):
        self.game = True

    def game_rurnning(self):
        return self.game

    def game_over(self):
        self.game = False

game = Game()

player = player.Player(screen.SCREEN_X / 2, screen.SCREEN_Y - 60, MIXER)
enemy = enemy.Enemy(random.randrange(0, screen.SCREEN_X - 50), -50)
boss = boss.Boss(300, -200)
health = lifebar.Health(screen.SCREEN_X - 150, 50, game)
collision_manage = collision_manager.collision_manage(health, player, enemy, boss)

TEXT = text.Text("GAMEOVER")

def draw():
    screen.SURFACE.fill(screen.BLACK)
    player.draw()
    enemy.draw()
    if boss:
        boss.draw()
    health.draw()
    pygame.display.update()

def update():
    global boss
    screen.CLOCK.tick(screen.FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit(1)

    draw()
    enemy.update()
    player.update()
    collision_manage.update()
    if boss:
        if not boss.dead:
            boss.update()
        else:
            boss = None



def run():
    while game.game_rurnning():
        update()
    while not game.game_rurnning():
        TEXT.draw()
        pygame.display.update()
        screen.SURFACE.fill(screen.BLACK)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                exit(1)


if __name__ == '__main__':
    run()

