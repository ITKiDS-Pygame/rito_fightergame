import pygame

SCREEN_X, SCREEN_Y = 640, 480
SCREEN = (SCREEN_X, SCREEN_Y)
SURFACE = pygame.display.set_mode(SCREEN)
FPS = 60
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORBOSS = (64, 64, 64)
fire_rate = 50
fire_timer = fire_rate
