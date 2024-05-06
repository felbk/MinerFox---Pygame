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
clock = pygame.time.Clock()
clock.tick(30)



ch1 = Chão((tela.get_width(),50),(0,tela.get_height() - 50 ),"Assets\provisorios\chao.png")

player = Player((150,150),(tela.get_width()/2,0))

Bd = False
Be = False

while play:

    tela.fill((255,255,255))

    #Analisa eventos
    for event in pygame.event.get():
        if event.type == QUIT:
           

            play = False
        if event.type == KEYDOWN:
            
                if event.key == K_d: 
                    Bd = True
                else:
                    Bd = False
                if event.key == K_a: 
                    Be = True
                else:
                    Be = False
                if event.key == K_ESCAPE:
                    play = False
        if event.type == KEYUP:
                if event.key == K_d: 
                    Bd = False
                if event.key == K_a: 
                    Be = False
        
                
       
    
        
    
   
    
    elementos.update()
    #allgnds.draw(tela)
    elementos.draw(tela)
    pygame.display.flip()
pygame.quit()
exit()



    
