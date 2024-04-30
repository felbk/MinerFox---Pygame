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
ch = Chão((0,0),50,50,tela)

while play:
    tela.fill(cor_tela)
    pygame.draw.rect(tela,(0,0,0),(ch.x,ch.y,ch.L,ch.A))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            play != play
            exit()
        #if event.type == KEYDOWN:

    
