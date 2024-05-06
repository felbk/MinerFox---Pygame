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
            self.vy = 4
        else:
            self.vy = 0
        

        #atualiza posição
        self.rect.y += self.vy
        self.rect.x += self.vx
        
        return

class Player(Corpo):
    def __init__(self,tam, pos):
        Corpo.__init__(self,tam,pos)
        fox = "Assets\-raposa\-idle\-idle (1).png"
        self.image = pygame.image.load(fox)
        self.image = pygame.transform.scale(self.image,self.tam)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.idle = True
        self.run = False
        self.idle_list= []
        self.die_list= []
        self.jump_list= []
        self.run_list= []
        self.frame= 0
        self.flip = False
        #Cria lista de frames da animação Idle
        for i in range(1,15):
            imgprov = pygame.image.load(f"Assets\-raposa\-idle\-idle ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            self.idle_list.append(imgprov)
        self.anim = self.idle_list
        #Cria lista de frames da animação Run
        for i in range(1,9):
            imgprov = pygame.image.load(f"Assets\-raposa\-run\-run ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            self.run_list.append(imgprov)
        
        

            


       
        
   
    
    def update(self):
    
        # Variaveis de controle=======================================================================
        from Principal import Be
        from Principal import Bd
        #Direita======================================================================================
        if Bd and self.andar :
            self.vx = 0.7
            if self.flip:
                self.flip = False
            if not self.run:
                self.frame=0
            self.run = True

        #Esquerda======================================================================================
        elif Be and self.andar :
            self.vx = -0.7
            if not self.flip:
                self.flip = True
            if not self.run:
                self.frame=0
            self.run = True
        #Parado============================================================================================
        else:
            self.vx= 0 
            if not self.idle:
                self.frame=0
            self.idle = True
            self.run = False
            

        #Analisa animação a ser executada==================================================================

       
        if self.idle:
            self.anim = self.idle_list
        if self.run:
            self.anim = self.run_list
        
        #Escolhe frame da animação======================================================================   
        self.image = self.anim[int(self.frame)]

        #Flipa imagem=====================================================================================
        if self.flip:
            self.image = pygame.transform.flip(self.image,1,0)
        

        #Progressão dos frames da animação==============================================================
        self.frame += 0.02 
        if self.frame >= len(self.anim):
            self.frame = 0

        
        Corpo.update(self)
        return

           
