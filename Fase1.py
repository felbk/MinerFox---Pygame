
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
    
    fase1 = Fase(tela,(4000,1000),matmapa) #Cria fase
    fase = 1
    while fase1.play:
        fase1.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(all_diamantes.sprites()) == 0 :
            fase1.play = False
            fase1.state = 0
            fase = 2
    elementos.empty()
    fase1.mixer.music.stop()
    return {"state": fase1.state , "fase": fase}

def Fase_2(tela):
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
    
    fase2 = Fase(tela,(len(matmapa[0])*100, len(matmapa) * 100),matmapa)

    

   
    fase = 2
    while fase2.play:
        fase2.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(all_diamantes.sprites()) == 0 :
            fase2.play = False
            fase2.state = 0
            fase =  3
    elementos.empty()
    fase2.mixer.music.stop()
    return {"state": fase2.state , "fase": fase}

def Fase_3(tela):
    D = "diamante"
    A = "ave"
    C = 14
    V = 15
    B = 1
    G = 12
    T = 21
    H = 16
    F = 13
    
    matmapa= [

 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, 0, 0, D, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, F, D, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, G, 0, 0, 0, 0, 0, D, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, C, V, B, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [B, G, 0, G, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, C, V, B, 0, 0, 0, 0, F, 0, 0, G, G, F, 0, 0, 0, A, 0, 0, 0, G, F, A, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, C, V, B, 0, 0, C, V, B, 0, 0, 0, F, F, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, G, G, G, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, H, A, 0, C, V, B, 0, 0],
 [0, H, 0, 0, 0, 0, 0, 0, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, 0, 0, G, A, T, 0, F, F, 0, G, 0, D],
 [F, T, G, 0, 0, F, D, A, 0, 0, F, T, G, 0, 0, 0, A, G, 0, C, V, V, V, V, V, V, V, V, V, V],
 [C, V, B, 0, 0, C, V, B, 0, 0, C, V, B, 0, 0, 0, C, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
    
    fase3 = Fase(tela,(len(matmapa[0])*100, len(matmapa) * 100),matmapa)

    fase = 3
    while fase3.play:
        fase3.update()
        if len(all_diamantes.sprites()) == 0 :
            fase3.play = False
            fase3.state = 0
            fase = 4

    elementos.empty()
    fase3.mixer.music.stop()
    return {"state": fase3.state , "fase": fase}
    
def Fase_4(tela):
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

    fase4 = Fase(tela,(4000,1000),matmapa4)
    
    fase=4
    while fase4.play:
        fase4.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(all_diamantes.sprites()) == 0 :
            fase4.play = False
            fase4.state = 0
            fase = 1
    elementos.empty()
    fase4.mixer.music.stop()
    return {"state": fase4.state , "fase": fase}

#cria fase 2

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
