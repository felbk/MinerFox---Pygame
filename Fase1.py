
def Fase_1():
    
    tela = pygame.display.set_mode((WIDTH,HEIGHT))
    play = True
    

    Chão((tela.get_width(),50),(0,tela.get_height() - 50 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,120),(0,tela.get_height() - 120 ),"Assets\provisorios\chao.png")

    player = Player((150,150),(tela.get_width()/2,0))

    vel = 2
    while play:

        tela.fill((255,255,255))

        #Analisa eventos
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                play = False

        keys = pygame.key.get_pressed()
        
            
        if keys[pygame.K_d]: 
            player.vx = vel
            player.flip = False   
        elif keys[pygame.K_a]: 
            player.vx = -vel 
            player.flip = True  
        else:
            player.vx = 0          
            
        if keys[pygame.K_ESCAPE]:
            play = False
        if keys[pygame.K_SPACE ] and not player.Fall :
            player.vy = -5
                      
                    
                    
                    

        elementos.update()
        elementos.draw(tela)
        pygame.display.flip()
    pygame.quit()
    return {"state": QUIT , "fase": 1}

    
#==============IMPORTS===============
from Config import WIDTH, HEIGHT
from sprites import *
import pygame
from pygame.locals import *
from sys import exit
from setup import QUIT , PARTIDA , HOME

