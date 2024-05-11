import pygame
import pygame.display
from pygame.locals import *
from sys import exit
from Config import WIDTH , HEIGHT , FPS

IDLE = 0
RUN = 1
JUMP = 2

elementos = pygame.sprite.Group()
allgnds = pygame.sprite.Group()
def mostra_mapa_na_tela(tela,mapa,player):
    mapa.fill((255,255,255))
    elementos.draw(mapa)
    tela.fill((255,255,255))

    pygame.Surface.blit(tela,mapa,(0,0),(player.colisor.rect.centerx - WIDTH/2,player.colisor.rect.centery - HEIGHT/2,WIDTH,HEIGHT))

    return 

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
   
   def __init__(self, tam = tuple, pos=tuple,img= pygame.SurfaceType) :
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.tam = tam
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.jump = False
        self.vx = 0
        self.vy = 0
        self.state = IDLE
        self.andar = True
        self.Fall = True
        self.flip= False
        self.colisor = pygame.sprite.Sprite
        self.colisor.rect = self.rect
        self.colisor.rect.center = self.rect.center
        self.add(elementos)
        
    
   
       
        
        

   def update(self):
       
        self.Fall = True
        g = 0.05 #aceleração da gravidade
        if self.vy < 3: #Velocidade maxima de queda
            self.vy += g

          #Movimento em y a ser analisado 
        self.colisor.proxima_posicao = pygame.Rect.copy(self.colisor.rect)
        self.colisor.proxima_posicao.y += self.vy
        colisao_Y = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.colisor.proxima_posicao):
                colisao_Y= True
                self.vy = 0
                if gnd.rect.y > self.colisor.rect.y : # colisão com limite no chão
                    self.Fall = False
                    self.colisor.rect.y= gnd.rect.y - self.colisor.rect.height
                if gnd.rect.y < self.colisor.rect.y : # colisão com limite no teto
                    self.Fall = True
                    self.colisor.rect.top = gnd.rect.bottom 
                
                break
        
        
        # permite o movimento caso não colida

        if not colisao_Y:
            self.colisor.rect.y = self.colisor.proxima_posicao.y
        #Movimento em x a ser analisado 
        self.colisor.proxima_posicao = pygame.Rect.copy(self.colisor.rect)
        self.colisor.proxima_posicao.x +=  self.vx
        colisao_X = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.colisor.proxima_posicao):
                colisao_X = True
                break
        
        # permite o movimento caso não colida

        if not colisao_X:
            self.colisor.rect.x = self.colisor.proxima_posicao.x

        # confere se não há mais onde cair
        passou_all_gnds = True
        for gnd in allgnds:
            if gnd.rect.y > self.colisor.rect.y-300:
                passou_all_gnds = False 
                break

        # caiu no void --> reposiciona
        if passou_all_gnds:
            self.colisor.rect.y = 0 
        

        #cola a imagem no colisor 
        
        self.rect.center = self.colisor.rect.center 
       


        
        return

    
        
class Player(Corpo):

    def __init__(self,tam, pos):
        fox = "Assets\-raposa\-idle\-idle (1).png"
        image = pygame.image.load(fox).convert_alpha()
        image = pygame.transform.scale(image,tam)
        image = image.subsurface((25,75),(100,75))
        Corpo.__init__(self,tam,pos,image)
        self.animacoes = {}
        self.animacoes["idle"]= []
        self.animacoes["jump"]= []
        self.animacoes["run"]= []
        self.animacoes["die"]= []
        self.frametick = 100
        self.frame= 0
        self.last_update = pygame.time.get_ticks()
        self.colisor.rect = pygame.Rect.inflate(self.colisor.rect,-50,-10)
        
        
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
            self.jump = False
        if self.vx != 0 and not self.Fall and not self.jump:
            self.state = RUN
            
        
        
     
        self.anima()
        Corpo.update(self)

        #ajeita raposa e colisor
        self.rect.centery -= 5
        if self.flip:
            self.rect.centerx +=16 #move a imagem em relação ao colisor
        else:
            self.rect.centerx -=16 #move a imagem em relação ao colisor
        
        return

    def anima(self):
               
        

        if self.state == RUN:
            if self.anim != self.animacoes["run"]:
                self.frame = 0
                self.frametick= 100
            self.anim = self.animacoes["run"]
        if self.state == JUMP:
            if self.anim != self.animacoes["jump"]:
                self.frame = 3
                self.frametick= 180
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
                    self.frame = 3
                    if self.vy >=0 : 
                        self.state = IDLE

        return

           
