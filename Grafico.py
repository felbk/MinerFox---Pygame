from Classes import*
import pygame
from pygame.locals import *
from sys import exit

def inicia_tela(L=int,A=int):
    pygame.display.init()
    tela = pygame.display.set_mode((L,A))
    
    return tela
