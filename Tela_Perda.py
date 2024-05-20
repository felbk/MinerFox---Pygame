import pygame
from os import path
from Config import WIDTH, HEIGHT
from Assets import load_assets
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def tela_perda(tela):
    #Carrega assets
    assets = load_assets()
    
    tempo_fps = pygame.time.Clock()
    #Carrega imagem e textos de perda
    tela_perda = assets['tela_perda']
    tela_perda_rect = tela_perda.get_rect()
    text_restart = assets['text_restart']
    text_esc = assets['text_esc']

    #Loop de tela de perda
    working = True
    while working:
        state = HOME
        tempo_fps.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                working = False
        
        #Volta para tela inicial
        if keys[pygame.K_ESCAPE]:
            state = False
            working = False
        
        #Reinicia a fase
        if keys[pygame.K_KP_ENTER]:
            state = True
            working = False

        #Desenha a tela e as escritas
        tela.blit(tela_perda,tela_perda_rect)
        tela.blit(text_restart,(WIDTH/2-462, 0.65*HEIGHT))
        tela.blit(text_esc,(WIDTH/2+57, 0.65*HEIGHT))
        pygame.display.flip()
    return state