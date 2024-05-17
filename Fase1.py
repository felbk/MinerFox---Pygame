
#função cria blocos do mapa


def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS

    fase1 = Fase(tela,(4000,1000)) #Cria fase
    

    Diamante((825,650))

#Cria os blocos do chão
    matmapa =[[0]*40]*10
    matmapa[5] = [0]*23 + ["ave"] + [ 0]*9 + ["ave"]
    matmapa[6] = [0]*21 + [14,15,15,15,1] + [0]*4 + [14,15,15,15,15,1] 
    matmapa[7] = [0]*5 +["ave"]+[0]*6 +["ave"] + [14,15,15,15,1] 
    matmapa[8] = [0]*7 + [2,3,4] + ["ave",0,0,0,0,"ave",0,0,0,"ave" ,0 ,0 ,0 ,"ave"] 
    matmapa[9] = [3]*7 + [6,7,8] + [0]*2+ [3]*20
    posiciona_itens_mapa(matmapa,(100,100))

    while fase1.play:
        fase1.update() # Atualiza fase
        # quando não houver mais aves, passa de fase
        if len(aves.sprites()) == 0 :
            fase1.play = False
            fase1.state = 0
    elementos.empty()
    return {"state": fase1.state , "fase": 1}


#==============IMPORTS===============

import pygame
from pygame.locals import *
from sys import exit
from sprites import *
from setup import QUIT , PLAYING , HOME


#carregando sons do jogo
pygame.mixer.music.load("songs\som__de_fundo.wav")
pygame.mixer.music.set_volume(0.4)
coleta_diamantes = pygame.mixer.Sound('songs\coleta_diamantes.mp3')
game_over_cacador = pygame.mixer.Sound('songs\game_over_cacador.wav')
game_over_jogo = pygame.mixer.Sound("songs\game_over.mp3")
som_aguia = pygame.mixer.Sound('songs\som_aguia.mp3')
som_cacador = pygame.mixer.Sound('songs\som_cacador.mp3')


