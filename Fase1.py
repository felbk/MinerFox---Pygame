#==============IMPORTS===============
from Grafico import *
from sprites import *
import pygame
from pygame.locals import *
from sys import exit
import random as rdm

pygame.init()
tela = pygame.display.set_mode((1280,720))
play = True
clock = pygame.time.Clock()
clock.tick(30)

Chão((tela.get_width(),50),(0,tela.get_height() - 50 ),"Assets\provisorios\chao.png")
Chão((tela.get_width()/2,120),(0,tela.get_height() - 120 ),"Assets\provisorios\chao.png")

player = Player((150,150),(tela.get_width()/2,0))

vel = 1
while play:

    tela.fill((255,255,255))

    #Analisa eventos
         
    for event in pygame.event.get():
        if event.type == QUIT:   
            play = False

        if event.type == KEYDOWN:
            
                if event.key == K_d: 
                   player.vx += vel
                   player.flip = False
                    
                if event.key == K_a: 
                    player.vx -= vel 
                    player.flip = True            
                    
                if event.key == K_ESCAPE:
                    play = False
                #if event.key == K_SPACE :
                      

                
                      
                           
                   
                
        if event.type == KEYUP:
                if event.key == K_d : 
                    player.vx -= vel
                    
                    
                if event.key == K_a : 
                    player.vx += vel
                
                if event.key == K_SPACE:
                     player.vy = 4
                
                

    elementos.update()
    elementos.draw(tela)
    pygame.display.flip()
pygame.quit()
exit()

    
