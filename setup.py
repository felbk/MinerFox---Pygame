
from sprites import Corpo , Player , Chão
import pygame
from pygame.locals import *
from sys import exit
from Fase1 import Fase_1
pygame.init()

HOME = 0 
PARTIDA = 1 
QUIT = 2
state = PARTIDA
fase = 1

while not state == QUIT:
   # if state == HOME:
        #Rodar tela inicial
        #state =  tela inicial( )["state"] -> função que retorna um dicionario com state e N da fase 
        

    if state == PARTIDA: 
        if fase == 1:
            dici = Fase_1()
            state = dici["state"]
            fase = dici["fase"]

pygame.quit()
exit()
        
