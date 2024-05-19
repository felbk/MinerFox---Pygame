import pygame
from os import path
from Config import WIDTH, HEIGHT
from Assets import load_assets
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def tela_perda(tela):
    assets = load_assets()
    tempo_fps = pygame.time.Clock()
    tela_inicial = assets['tela_inicial']
    tela_inicial_rect = tela_inicial.get_rect()
    text_restart = assets['text_restart']
    text_esc = assets['text_esc']

    working = True
    while working:
        state = HOME
        tempo_fps.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                working = False
        
        if keys[pygame.K_ESCAPE]:
            state = False
            working = False
        if keys[pygame.K_KP_ENTER]:
            state = True
            working = False


        tela.blit(tela_inicial,tela_inicial_rect)
        tela.blit(text_restart,(WIDTH/2-462, 0.65*HEIGHT))
        tela.blit(text_esc,(WIDTH/2+57, 0.65*HEIGHT))
        pygame.display.flip()
    return state