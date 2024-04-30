from Classes import*
import pygame
from pygame.locals import *
from sys import exit

def inicia_tela(L=int,A=int):
    tela = pygame.display
    tela.init()
    tela.set_mode((L,A))
    return tela
