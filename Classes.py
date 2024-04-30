import pygame
from pygame.locals import *
from sys import exit
import random as rdm

class Chão:
    def __init__(self,pos=tuple,L=int,A=int,surf="superficie/tela"):
        self.x = pos[0]
        self.y = pos[1]
        self.L = L
        self.A = A
        self.surf = surf
