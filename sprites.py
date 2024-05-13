import pygame
import pygame.display
import pygame.display
from pygame.locals import *
from sys import exit
from Config import WIDTH , HEIGHT , FPS

IDLE = 0
RUN = 1
JUMP = 2

elementos = pygame.sprite.Group()
allgnds = pygame.sprite.Group()
hud = pygame.sprite.Group()

def posicao_mapa(matriz_mapa,tamanho):
    for linha in range(len(matriz_mapa)):
        for coluna in range(len(matriz_mapa[linha])):
            elemento = matriz_mapa[linha][coluna]
            posicao = (coluna*tamanho[0], linha*tamanho[1])
            if elemento in range (1,16):
                img = f"Assets/-mapa/-mapa ({elemento}).png"
                Chão(tamanho,posicao,img)

            
    return 

class Fase ():
    def __init__(self,tela,tamanho_mapa= tuple):
        self.mapa = pygame.Surface(tamanho_mapa)
        self.player = Player((150,150),(10,0))
        self.play = True 
        self.vel = 2
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        self.tela = tela
        self.bg = pygame.image.load("Assets/-mapa/bg.png")
        self.bg = pygame.transform.scale(self.bg,(self.tela.get_size()))
        self.pos_cam = (0,0)

    def analisa_controles(self):
          #Analisa eventos
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        
            
        if keys[pygame.K_d]: 
            self.player.vx = self.vel
            self.player.flip = False   
        elif keys[pygame.K_a]: 
            self.player.vx = -self.vel 
            self.player.flip = True  
        else:
            self.player.vx = 0          
            
        if keys[pygame.K_ESCAPE]:
             self.play = False
        if keys[pygame.K_SPACE ] and not self.player.Fall :
            self.player.vy = -5
            self.player.jump = True
        if not keys[pygame.K_SPACE ]:
            self.player.jump = False

        #nao ultrapassa limites do mapa
        if self.player.rect.left < 0 :
            self.player.vx =1         
        if self.player.rect.right > self.mapa.get_width() :
            self.player.vx=-1
        if self.player.lives_player <=0:
            self.play = False
        return
    
    def bloqueia_limites(self):
          #nao ultrapassa limites do mapa
        if self.player.rect.left < 0 :
            self.player.vx =1         
        if self.player.rect.right > self.mapa.get_width() :
            self.player.vx=-1
        return
    
    def camera_movimenta(self):
   
        self.pos_cam=pygame.Rect(self.player.colisor.rect.centerx - WIDTH/2,self.player.colisor.rect.centery - HEIGHT/2,WIDTH,HEIGHT)
        #barra camera ao chegar na esq
        if self.pos_cam.left < 0 : 
            self.pos_cam.left = 0
        #barra camera ao chegar na dir    
        if self.pos_cam.right > self.mapa.get_width() : 
            self.pos_cam.right = self.mapa.get_width()
        #barra camera ao chegar no topo
        if self.pos_cam.top < 0 : 
            self.pos_cam.top= 0
        #barra camera ao chegar em baixo 
        if self.pos_cam.bottom > self.mapa.get_height() : 
            self.pos_cam.bottom = self.mapa.get_height()

        
        pygame.Surface.blit(self.tela,self.mapa,(0,0),self.pos_cam)

        return 
    def update(self):
        elementos.update()
        hud.update()
        self.mapa.fill((255,255,255))
        self.analisa_controles()
        self.bloqueia_limites()
       
        pygame.Surface.blit(self.mapa,self.bg,(self.pos_cam[0],self.pos_cam[1]))
        elementos.draw(self.mapa)
        self.tela.blit(self.player.txt_live,(300,300))
        hud.draw(self.tela)
        self.camera_movimenta()
        self.tela.blit(self.player.txt_live,(50,0.9*HEIGHT))
        pygame.display.flip()
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
            self.passou_all_gnds = True
        else:
            self.passou_all_gnds = False
        

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
        self.lives_player = 3
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

        if self.passou_all_gnds == True:
            self.lives_player -=1
            self.colisor.rect.y = 0

        self.fonte = pygame.font.Font('Assets/-interacoes/Hearts Salad.otf',48)
        self.txt_live = self.fonte.render('N' * self.lives_player, True, (255,0,0))
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

           
