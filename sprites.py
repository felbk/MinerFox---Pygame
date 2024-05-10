import pygame
from pygame.locals import *
from sys import exit

IDLE = 0
RUN = 1
JUMP = 2

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
        self.jump = False
        self.vx = 0
        self.vy = 0
        self.state = IDLE
        self.add(elementos)
        self.andar = True
        self.Fall = True
        

   def update(self):
        self.Fall = True
        g = 0.05
        self.vy += g
          #Movimento em y a ser analisado 
        self.proxima_posicao = pygame.Rect.copy(self.rect)
        self.proxima_posicao.y += self.vy
        colisao_Y = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.proxima_posicao):
                colisao_Y= True
                self.vy = 0
                if gnd.rect.y > self.rect.y :
                    self.Fall = False
                    self.rect.y= gnd.rect.y - self.rect.height
                
                break
        
        
        # permite o movimento caso não colida

        if not colisao_Y:
            self.rect.y = self.proxima_posicao.y
        #Movimento em x a ser analisado 
        self.proxima_posicao = pygame.Rect.copy(self.rect)
        self.proxima_posicao.x +=  self.vx
        colisao_X = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.proxima_posicao):
                colisao_X = True
                break
        
        # permite o movimento caso não colida

        if not colisao_X:
            self.rect.x = self.proxima_posicao.x
        
        
        return

class Player(Corpo):
    def __init__(self,tam, pos):
        Corpo.__init__(self,tam,pos)
        fox = "Assets\-raposa\-idle\-idle (1).png"
        self.image = pygame.image.load(fox).convert_alpha()
        self.image = pygame.transform.scale(self.image,self.tam)
        self.image = self.image.subsurface((25,75),(100,75))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] 
        self.rect.y = self.pos[1]
        self.animacoes = {}
        self.animacoes["idle"]= []
        self.animacoes["jump"]= []
        self.animacoes["run"]= []
        self.animacoes["die"]= []
        self.frametick = 100
        self.frame= 0
        self.flip = False
        self.last_update = pygame.time.get_ticks()
        
        #Cria lista de frames da animação Idle
        for i in range(1,15):
            imgprov = pygame.image.load(f"Assets\-raposa\-idle\-idle ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            imgprov =  imgprov.subsurface((25,75),(100,75))
            self.animacoes["idle"].append(imgprov)
        self.anim = self.animacoes["idle"]
        #Cria lista de frames da animação Run
        for i in range(1,9):
            imgprov = pygame.image.load(f"Assets\-raposa\-run\-run ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            imgprov =  imgprov.subsurface((25,75),(100,75))
            self.animacoes["run"].append(imgprov)
        #Cria lista de frames da animação Jump
        for i in range(1,8):
            imgprov = pygame.image.load(f"Assets\-raposa\-jump\-jump ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            imgprov =  imgprov.subsurface((25,75),(100,75))
            self.animacoes["jump"].append(imgprov)


     

        


    
    def update(self):
        
        
        if self.jump:
            self.state = JUMP
        if self.vx == 0 and not self.Fall and self.vy == 0:
            self.state = IDLE
        if self.vx != 0 and not self.Fall and not self.jump:
            self.state = RUN
        
        
     
        self.anima()
        Corpo.update(self)
        
        return

    def anima(self):
               
        

        if self.state == RUN:
            if self.anim != self.animacoes["run"]:
                self.frame = 0
                self.frametick= 100
            self.anim = self.animacoes["run"]
        if self.state == JUMP:
            if self.anim != self.animacoes["jump"]:
                self.frame = 2
                self.frametick= 100
            self.anim = self.animacoes["jump"]
        if self.state == IDLE:
            if self.anim != self.animacoes["idle"]:
                self.frame = 0
                self.frametick= 100
            self.anim = self.animacoes["idle"]

        self.image = self.anim[int(self.frame)]
        if self.flip:
            self.image = pygame.transform.flip(self.image,1,0)
        
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frametick:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.anim):
                self.frame = 0 
                if self.anim == self.animacoes["jump"]:
                    self.frame = 2

        return

           
