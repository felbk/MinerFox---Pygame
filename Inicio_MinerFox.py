import pygame
from os import path
from Config import WIDTH, HEIGHT
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def inicio_minerfox(tela):
    tempo_fps = pygame.time.Clock()
    tela_inicial = pygame.image.load('Assets/-tela_inicial/-tela_inicio_Miner_Fox.png').convert()
    tela_inicial = pygame.transform.scale(tela_inicial,(WIDTH,HEIGHT))
    tela_inicial_rect = tela_inicial.get_rect()

    working = True
    while working:
        tempo_fps.tick(FPS)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                working = False
        if keys[pygame.K_KP_ENTER]:
            state = PLAYING
            working = False
        if keys[pygame.K_ESCAPE]:
            state = QUIT
            working = False
        tela.blit(tela_inicial,tela_inicial_rect)
        pygame.display.flip()
    return state



