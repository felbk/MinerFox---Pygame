
#função cria blocos do mapa
def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS
    D = 'diamante'
    A = 'ave'
    #Cria os blocos do chão
    matmapa =[[0]*40]*10
    matmapa[5] = [0]*23 + [A] + [0]*9 + [A] + [D]
    matmapa[6] = [0]*21 + [14,15,15,15,1] + [0]*3 + [D] + [14,15,15,15,15,1] 
    matmapa[7] = [0]*5 +[A]+[0]*6 +[A] + [14,15,15,15,1] 
    matmapa[8] = [0,12,0,12,0,13,13] + [2,3,4] + [A,0,0,D,0,0,A,0,0,0,A ,0, D, 0 ,0 ,A] 
    matmapa[9] = [3]*7 + [6,7,8] + [0]*2+ [3]*20
    
    FASE = Fase(tela,(4000,1000),matmapa) #Cria fase
    FASE.fase = 1 
    while FASE.play:
        FASE.update() # Atualiza fase
        # quando não houver mais diamantes passa de fase
        if len(all_diamantes.sprites()) == 0 :
            FASE.play = False
            FASE.state = 0
            FASE.fase += 1
    elementos.empty()
    FASE.mixer.music.stop()
    return {"state": FASE.state , "fase": FASE.fase}

def Fase_2(tela):
    #Define os itens utilizados
    D = "diamante"
    A = "ave"
    C = 14
    V = 15
    B = 1
    G = 12
    T = 21
    H = 16
    F = 13
    L = 36
    #Mapa 2 por extenso
    matmapa= [
 [0, 0, 0, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, A, D, T, 0, 0, 0, 0, 0, 0, 0, 0, 0, T, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, C, V, B, 0, H, 0, A, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, T, D, 0, 0, 0, 0, A, 0, 0, 0, 0, 0, 0, A, T, 0, 0, 0, 0, A, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, C, V, B, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, D, 0, 0, 0],
 [0, 0, 0, 0, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, V, B, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, H, 0, 0, 0, H, 0, 0, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, A, T, 0, 0, 0, T, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, D, L, 0, V],
 [0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0],
 [0, 0, H, 0, 0, D, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, 0, 0, 0, 0, 0, 0],
 [0, L, T, 0, C, V, B, 0, 0, 0, 0, V, V, 0, 0, 0, 0, 0, D, L, 0, 0, C, V, B, 0, 0, 0, 0, 0],
 [C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
    
    FASE = Fase(tela,(len(matmapa[0])*100, len(matmapa) * 100),matmapa) #cria mapa 2

    FASE.fase = 2
    while FASE.play:
        FASE.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(all_diamantes.sprites()) == 0 :
            FASE.play = False
            FASE.state = 0
            FASE.fase += 1
    elementos.empty()
    FASE.mixer.music.stop()
    return {"state": FASE.state , "fase": FASE.fase}

def Fase_3(tela):
    #atalhos para criação da matriz mapa
    D = "diamante"
    A = "ave"
    C = 14
    V = 15
    B = 1
    G = 12
    T = 21
    H = 16
    F = 13
    #Mapa 3 
    matmapa= [[0]*100]*10
    matmapa[7] = [H,0,0,D,0,0,0,0,0,0,0,D,H,0,0,0,0,0,0,0,0,0,0,0,D]*4
    matmapa[8] = [T,G,F,0,G,G,G,G,0,0,0,0,T,0,G,0,F,F,F,0,0,G,G,0,F]*4
    matmapa[9] = [3]*100
    
    FASE = Fase(tela,(len(matmapa[0])*100, len(matmapa) * 100),matmapa)

    FASE.fase = 3
    ultimoupdate= pygame.time.get_ticks()
    while FASE.play:
        now = pygame.time.get_ticks()
        delta = now - ultimoupdate
        intervalo = random.choice([700,1600,1500,2000,2500,])
        alturasort = random.choice([200,210,260,220,300,350,400])
        if delta >= intervalo:
            Ave((FASE.pos_cam[0]+WIDTH,FASE.mapa.get_height()-alturasort)).ciclo = False
            ultimoupdate = now
            for ave in aves:
                if ave.rect.x < FASE.pos_cam[0]:
                    ave.kill()

        FASE.update()
        if len(all_diamantes.sprites()) == 0 :
            FASE.play = False
            FASE.state = 0
            FASE.fase += 1

            

    elementos.empty()
    FASE.mixer.music.stop()
    return {"state": FASE.state , "fase": FASE.fase}
    
def Fase_4(tela):
    #Define os itens utilizados
    D = 'diamante'
    A = 'ave'
    C = 14
    V = 15
    B = 1
    G = 12
    T = 22
    H = 23
    F = 13
    M = 28
    #Mapa 4 por extenso
    matmapa4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, 0, 0, G, 29, 0, 0, 0, 0, 0, 0, H, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, C, V, V, B, 0, 0, 0, 0, F, T, D, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, G, T, F, D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, D, 0, 0, 0, 0, 25, 0, 0, 0, C, V, V,B, 0, 0, 0, 0, H, 0, 0, 0, A, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, G, T, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, G, T, 0, 0, C, V, B, 0, 0, F, G, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 26, 0, 0, C, V, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, B, 0, 0, 0, 0, 0, 0, 0, C, B, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, M, F, T, D, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, H, 0, 0,C, V, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,3 , 0, 0],
    [36, G, T, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, D, 0, 0, 0, 0, 0, 6, 0, 0, 0],
    [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 0, 0, 0]]

    FASE = Fase(tela,(4000,1000),matmapa4) #Cria tamanho da fase
    
    FASE.fase=4
    while FASE.play:
        FASE.update() # Atualiza fase
        # quando não houver mais diamantes
        if len(all_diamantes.sprites()) == 0 :
            FASE.play = False
            FASE.state = 0
            FASE.fase += 1
           
    elementos.empty()
    FASE.mixer.music.stop()
    return {"state": FASE.state , "fase": FASE.fase}

#==============IMPORTS===============

import pygame
from pygame.locals import *
from sys import exit
from sprites import *
from setup import QUIT , PLAYING , HOME
from Assets import load_assets

#carrega assets
assets = load_assets()

#carregando sons do jogo
pygame.mixer.music.load("songs\som__de_fundo.wav")
pygame.mixer.music.set_volume(0.4)
coleta_diamantes = assets['coleta_diamantes']
game_over_cacador = assets['game_over_cacador']
game_over_jogo = assets['game_over_jogo']
som_aguia = assets['som_aguia']
som_cacador = assets['som_cacador']


assets["Placar"] = pygame.font.Font('assets/-fontes/fonte_arcade')
