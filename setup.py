
from sprites import Corpo , Player , Chão
from Config import WIDTH,HEIGHT, FPS
import pygame
from pygame.locals import *
from sys import exit
from Fase1 import Fase_1, Fase_2, Fase_3, Fase_4, Fase_4
from Inicio_MinerFox import inicio_minerfox
pygame.init()
#Define o tamanho da tela
tela = pygame.display.set_mode((WIDTH,HEIGHT))

#Define variaveis referentes ao jogo

HOME = 0 #Começa na tela inicial
PLAYING = 1 #Esta jogando
QUIT = 2 #Estado de sair do jogo
state = HOME # Jogo começa na tela inicial
fase = 1 # Jogo começa na fase 1


#Loop principal 
while not state == QUIT:
    if state == HOME:
        #Rodar tela inicial
        state = inicio_minerfox(tela)
        #state =  tela inicial( )["state"] -> função que retorna um dicionario com state e N da fase 
    elif state == PLAYING: 
        #Fase 1
        if fase == 1:
            dici = Fase_1(tela)
            state = dici["state"]
            fase = dici["fase"]
        #Fase 2
        if fase == 2:
            dici = Fase_2(tela)
            state = dici["state"]
            fase = dici["fase"]
        #Fase 3
        if fase == 3:
            dici = Fase_3(tela)
            state = dici["state"]
            fase = dici["fase"]
        #Fase 4
        if fase == 4:
            dici = Fase_4(tela)
            state = dici["state"]
            fase = dici["fase"] 
#Sair do pygame
pygame.quit()

        
