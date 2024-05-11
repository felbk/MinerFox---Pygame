

def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS

    fase1 = Fase(tela,(2000,2000))

    Chão((tela.get_width(),50),(800,fase1.mapa.get_height() - 50 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,120),(0,fase1.mapa.get_height() - 120 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,50),(500,fase1.mapa.get_height() - 320 ),"Assets\provisorios\chao.png")

    while fase1.play:
        fase1.update()
        
    elementos.empty()
    return {"state": 0 , "fase": 1}


#==============IMPORTS===============

import pygame
from pygame.locals import *
from sys import exit
from sprites import *
from setup import QUIT , PLAYING , HOME

