
from sprites import Corpo , Player , Chão
from Config import WIDTH,HEIGHT, FPS
import pygame
from pygame.locals import *
from sys import exit
from Fase1 import Fase_1
pygame.init()
tela = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)


HOME = 0
PLAYING = 1
QUIT = 2
state = PLAYING
fase = 1


while not state == QUIT:
   # if state == HOME:
        #Rodar tela inicial
        #state =  tela inicial( )["state"] -> função que retorna um dicionario com state e N da fase 
        

    if state == PLAYING: 
        if fase == 1:
            dici = Fase_1(tela)
            state = dici["state"]
            fase = dici["fase"]

pygame.quit()

        
