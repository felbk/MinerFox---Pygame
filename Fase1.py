
#função cria blocos do mapa


def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS

#Cria os blocos do chão
    matmapa =[[0]*40]*10
    matmapa[5] = [0]*23 + ["ave"] + [0]*9 + ["ave"] + ["diamante"]
    matmapa[6] = [0]*21 + [14,15,15,15,1] + [0]*3 + ["diamante"] + [14,15,15,15,15,1] 
    matmapa[7] = [0]*5 +["ave"]+[0]*6 +["ave"] + [14,15,15,15,1] 
    matmapa[8] = [0,12,0,12,0,13,13] + [2,3,4] + ["ave",0,0,"diamante",0,0,"ave",0,0,0,"ave" ,0, "diamante", 0 ,0 ,"ave"] 
    matmapa[9] = [3]*7 + [6,7,8] + [0]*2+ [3]*20
    
    fase1 = Fase(tela,(4000,1000),matmapa) #Cria fase
    

    


    while fase1.play:
        fase1.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(all_diamantes.sprites()) == 0 :
            fase1.play = False
            fase1.state = 0
    elementos.empty()
    fase1.mixer.music.stop()
    return {"state": fase1.state , "fase": 1}

def Fase_3(tela):
    D = "diamante"
    A = "ave"
    C = 14
    V = 15
    B = 1
    matmapa= [

 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, C, V, B, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, C, V, B, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, B, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, C, V, V, V, V, V, V, V, V, V, V],
 [C, V, B, 0, 0, C, V, B, 0, 0, C, V, B, 0, 0, 0, C, B, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
    
    fase3 = Fase(tela,(len(matmapa[0])*100, len(matmapa) * 100),matmapa)

    while fase3.play:
        fase3.update()


    elementos.empty()
    fase3.mixer.music.stop()
    return {"state": fase3.state , "fase": 1}
    


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
