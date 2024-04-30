import pygame

from pygame.locals import *
from sys import exit
import random as rdm

elementos = pygame.sprite.Group()
allgnds = pygame.sprite.Group()

class Chão(pygame.sprite.Sprite):
    def __init__(self, tam = tuple, pos=tuple) :
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.tam = tam
        self.rect = (pos[0],pos[1],tam[0],tam[1])
        self.add(allgnds)
        self.add(elementos)

    def update(self):

        return 

        

class Corpo(pygame.sprite.Sprite):
   
   def __init__(self, tam = tuple, pos=tuple) :
        pygame.sprite.Sprite.__init__(self)
        self.x=pos[0]
        self.y=pos[1]
        self.pos = (self.x,self.y)
        self.tam = tam
        self.rect = Rect(pos , tam)
        self.add(elementos)

        

   def update(self):
        self.Fall = True

        for gnd in allgnds:
            if  pygame.sprite.collide_rect(self,gnd):
                self.Fall= False
        if self.Fall == True:    
            self.y += 2
            self.pos = (self.x,self.y)
            self.rect = Rect(self.pos , self.tam)
       
        return
           
