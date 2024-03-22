import pygame

class Mixer:
    def __init__(self):
        #BGM pygame.mixer.music.load("ファイル名/中身")
        pygame.mixer.music.load("music/rito_BGM.wav")
        #効果音 pygame.mixer.music.load("ファイル名/中身")
        self.shot = pygame.mixer.Sound("music/ビーム砲1.mp3")

    def shoot_laser(self):
        self.shot.play() #再生

    def music(self):
        pygame.mixer.music.play(-1) #ループ再生