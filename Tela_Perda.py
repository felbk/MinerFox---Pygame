import pygame
from os import path
from Config import WIDTH, HEIGHT
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def tela_perda(tela):
    tempo_fps = pygame.time.Clock()
    tela_inicial = pygame.image.load('Assets/-tela_final/-tela_final.jpg').convert()
    tela_inicial = pygame.transform.scale(tela_inicial,(WIDTH,HEIGHT))
    tela_inicial_rect = tela_inicial.get_rect()
    start_text = pygame.font.Font('Assets/-interacoes/Alfabeto.ttf',35)
    text_restart = start_text.render('Press Enter to Restart',True,(255,255,255))
    text_esc = start_text.render('Press Esc to Exit', True, (255,255,255))

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
            state = HOME
            working = False
        if keys[pygame.K_KP_ENTER]:
            state = PLAYING
            working = False


        tela.blit(tela_inicial,tela_inicial_rect)
        tela.blit(text_restart,(WIDTH/2-462, 0.65*HEIGHT))
        tela.blit(text_esc,(WIDTH/2+57, 0.65*HEIGHT))
        pygame.display.flip()
    return state