import pygame
from pygame.locals import *
from sys import exit
import random as rdm


elementos = pygame.sprite.Group()
allgnds = pygame.sprite.Group()

class Chão(pygame.sprite.Sprite):
    def __init__(self, tam = tuple, pos=tuple,img=str) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.pos = pos
        self.tam = tam
        self.image = pygame.transform.scale(self.image,self.tam)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.add(allgnds)
        self.add(elementos)

        return
    
    

        

class Corpo(pygame.sprite.Sprite):
   
   def __init__(self, tam = tuple, pos=tuple) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos , tam)
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.pos = (self.rect.x,self.rect.y)
        self.tam = tam
        self.vx = 0
        self.vy = 0
        self.andar = True
        self.add(elementos)

    
  

   def update(self):
        self.Fall = True
        self.andar = True
        # Confere se está no chão ou caindo
        
        
        for colisor in pygame.sprite.spritecollide(self,allgnds,dokill=False):
                if  colisor.rect.clipline((self.rect.bottomleft),(self.rect.bottomright)):
                    self.Fall= False
                if  colisor.rect.collidepoint(self.rect.midleft):
                    self.andar = False
                    self.vx = 0.1
                if  colisor.rect.collidepoint(self.rect.midright):
                    self.andar = False
                    self.vx = -0.1
        
                
                
                
                
                    
        if self.Fall == True:
            self.vy = 2.5
        else:
            self.vy = 0
        

        #atualiza posição
        self.rect.y += self.vy
        self.rect.x += self.vx
        
        return

class Player(Corpo):
    def __init__(self,tam, pos):
        Corpo.__init__(self,tam,pos)
        fox = "Assets\-raposa\idle\-tile014.png"
        self.image = pygame.image.load(fox)
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300


       
        
   
    
    def update(self):
    
        # Controle para andar
        from Principal import Be
        from Principal import Bd
        
        if Bd and self.andar :
            self.vx = 0.7
            
        elif Be and self.andar :
            self.vx = -0.7
            
        else:
            self.vx= 0 
        
        Corpo.update(self)
        return

           
