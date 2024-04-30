#==============IMPORTS===============
from Grafico import *
from Classes import *
import pygame
from pygame.locals import *
from sys import exit
import random as rdm

pygame.init()
tela = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0],FULLSCREEN)

play = True

while play:
    pygame.display.flip()
    tela.fill((255,255,255))

    #Analisa eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            play = False
            pygame.quit()
            exit()
        
    




    
