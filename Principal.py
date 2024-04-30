from Grafico import *
from Classes import *
import pygame
from pygame.locals import *
from sys import exit
import random as rdm

pygame.init()
tela=inicia_tela(500,500)
cor_tela= (0,0,150)
play = True

while play:
    tela.fill(cor_tela)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            play != play
            exit()
        if event.type == KEYDOWN:

    
