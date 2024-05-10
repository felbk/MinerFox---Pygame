
def Fase_1():
    pygame.init()
    tela = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
    play = True
    clock = pygame.time.Clock()
    clock.tick(FPS)

    Chão((tela.get_width(),50),(0,tela.get_height() - 50 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,120),(0,tela.get_height() - 120 ),"Assets\provisorios\chao.png")

    player = Player((150,150),(tela.get_width()/2,0))

    vel = 2
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
                    if event.key == K_SPACE :
                        player.vy = -6
                        

                    
                        
                            
                    
                    
            if event.type == KEYUP:
                    if event.key == K_d : 
                        player.vx -= vel
                        
                        
                    if event.key == K_a : 
                        player.vx += vel
                    
                    if event.key == K_SPACE:
                        player.vy = 5
                    
                    

        elementos.update()
        elementos.draw(tela)
        pygame.display.flip()
    pygame.quit()
    return {"state": QUIT , "fase": 1}

    
#==============IMPORTS===============
from Config import WIDTH, HEIGHT, FPS
from sprites import *
import pygame
from pygame.locals import *
from sys import exit
from setup import QUIT , PARTIDA , HOME

