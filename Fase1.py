
#função cria blocos do mapa


def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS

    fase1 = Fase(tela,(4000,1000)) #Cria fase
    Ave((500,800))

    Diamante((825,650))

#Cria os blocos do chão
    matmapa =[[0]*40]*10

    matmapa[6] = [0]*21 + [14,15,15,15,1] + [0]*4 + [14,15,15,15,15,1] 
    matmapa[7] = [0]*13 + [14,15,15,15,1] 
    matmapa[8] = [0]*7 + [2,3,4] 
    matmapa[9] = [3]*7 + [6,7,8] + [0]*2+ [3]*20
    posicao_mapa(matmapa,(100,100))

    while fase1.play:
        fase1.update() # Atualiza fase
        
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


