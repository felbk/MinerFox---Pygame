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




ch1 = Chão((tela.get_width(),50),(0,tela.get_height() - 50 ))
ch2 = Chão((tela.get_width()/2,50),(100,tela.get_height() -500 ))
corpo1 = Corpo((50,50),(tela.get_width()/2,0))
corpo1.add(elementos)




while play:

    tela.fill((255,255,255))

    #Analisa eventos
    for event in pygame.event.get():
        if event.type == QUIT:
           

            play = False
            pygame.quit()
            exit()
    
        
    
    pygame.draw.rect(tela,(0,0,0),ch1.rect)
    pygame.draw.rect(tela,(0,0,0),ch2.rect)
    pygame.draw.rect(tela,(255,0,0),corpo1.rect)
    
    elementos.update()
    pygame.display.flip()



    
