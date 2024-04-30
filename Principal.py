from Grafico import *
from Classes import *
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
tela=inicia_tela(500,500)

play = True

while play:
    tela.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play != play
            exit()
    
