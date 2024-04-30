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
        self.vx = 0
        self.vy = 0
        self.add(elementos)

        

   def update(self):
        
        self.Fall = True
        from Principal import Be
        from Principal import Bd

        if Bd:
            self.vx = 0.5
        elif Be:
            self.vx = -0.5
        else:
            self.vx= 0 
            
        # Confere se está no chão ou caindo
        for gnd in allgnds:
            if  pygame.sprite.collide_rect(self,gnd):
                self.Fall= False
                    
        if self.Fall == True:
            self.vy = 2
        else:
            self.vy = 0

        #atualiza posição
        self.y += self.vy
        self.x += self.vx
        self.pos = (self.x,self.y)
        self.rect = Rect(self.pos , self.tam)
        
        return

class Player(Corpo):
    def __init__(self,tam, pos):
        Corpo.__init__(self,tam,pos)
        

    def update(self):
        # Controle para andar
        from Principal import Be
        from Principal import Bd

        if Bd:
            self.vx = 0.5
        elif Be:
            self.vx = -0.5
        else:
            self.vx= 0 
        Corpo.update(self)
        return

           
