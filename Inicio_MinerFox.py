import pygame
from os import path
from Config import WIDTH, HEIGHT
from Assets import load_assets
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def inicio_minerfox(tela):
    #Carrega assets
    assets = load_assets()
    pygame.mixer.init()
    
    tempo_fps = pygame.time.Clock()
    #Carrega imagens e textos da tela inicial
    tela_inicial = assets['tela_inicial']
    tela_inicial_rect = tela_inicial.get_rect()
    text = assets['text']
    #Loop da tela inicial
    working = True
    while working:
        state = HOME
        tempo_fps.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                working = False
            if event.type == pygame.KEYDOWN:
                #Fecha o jogo
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
            working = False

        #Inicial game
        if keys[pygame.K_KP_ENTER]:
            state = PLAYING
            working = False

        #Desenha tela perda
        tela.blit(tela_inicial,tela_inicial_rect)
        tela.blit(text,(WIDTH/2 - 262, 0.675*HEIGHT))
        pygame.display.flip()
    return state



