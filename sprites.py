import pygame
import pygame.display
import pygame.display
from pygame.locals import *
import random
from sys import exit
from Config import WIDTH , HEIGHT , FPS
from Tela_Perda import tela_perda
from Assets import load_assets
IDLE = 0
RUN = 1
JUMP = 2


elementos = pygame.sprite.Group()
allgnds = pygame.sprite.Group()
hud = pygame.sprite.Group()
allcoliders = pygame.sprite.Group()
all_diamantes = pygame.sprite.Group()
aves = pygame.sprite.Group()



def posiciona_itens_mapa(matriz_mapa,tamanho):
    for linha in range(len(matriz_mapa)):
        for coluna in range(len(matriz_mapa[linha])):
            elemento = matriz_mapa[linha][coluna]
            posicao = (coluna*tamanho[0], linha*tamanho[1])
            if elemento in range (1,16):
                img = f"Assets/-mapa/-mapa ({elemento}).png"
                if elemento not in range(12,14): #Chão sem fisica
                    Chão(tamanho,posicao,img)
                else:
                    Chão(tamanho,posicao,img,False)
            if elemento == "ave" : 
                Ave(posicao)
            

            
    return 

class Fase ():
    def __init__(self,tela,tamanho_mapa= tuple,matmapa="matriz"):
        self.mapa = pygame.Surface(tamanho_mapa)
        posiciona_itens_mapa(matmapa,(100,100))
        self.player = Player((150,150),(10,0))
        self.play = True 
        self.vel = 2
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        self.tela = tela
        self.bg = pygame.image.load("Assets/-mapa/bg.png")
        self.bg = pygame.transform.scale(self.bg,(self.tela.get_size()))
        self.pos_cam = (0,0)
        self.state = 1
        self.cont_aves = len(aves.sprites())
        
        
    def analisa_colisoes(self):
        for ave in pygame.sprite.spritecollide(self.player,aves,True, pygame.sprite.collide_mask):
            if pygame.sprite.collide_mask(self.player,ave):
                if self.player.rect.centery < ave.rect.centery :
                
                    self.player.vy = -3
                    self.player.score +=100
                else:
                    self.player.lives_player -=1
                    self.player.rect.bottom = ave.rect.top-10
                    self.player.vy = -5 
                break
                
                
        return

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
             self.state = 0
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
            tela_perda(self.tela)
            if tela_perda == True:
                self.play = True
                self.state = 1
            else: 
                self.play=False
                self.state = 0
        return
    
    def bloqueia_limites(self):
          #nao ultrapassa limites do mapa
        if self.player.rect.left < 0 :
            self.player.vx =1         
        if self.player.rect.right > self.mapa.get_width() :
            self.player.vx=-1
        return
    
    def camera_movimenta(self):
   
        self.pos_cam=pygame.Rect(self.player.rect.centerx - WIDTH/2,self.player.rect.centery - HEIGHT/2,WIDTH,HEIGHT)
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
        self.fonte_ave = pygame.font.Font('Assets\-interacoes\Alfabeto.ttf',48)
        self.txt_cont_aves = self.fonte_ave.render('{0}'.format(self.cont_aves),True, (255,255,255))

        return 
    def hud_update(self):
        self.fonte_ave = pygame.font.Font('Assets\-interacoes\Alfabeto.ttf',48)
        self.txt_cont_aves = self.fonte_ave.render('{0}'.format(self.cont_aves),True, (255,255,255))
        return
    def update(self):
        elementos.update()
        allcoliders.update()
        hud.update()
        self.mapa.fill((255,255,255))
        self.analisa_colisoes()
        self.analisa_controles()
        self.bloqueia_limites()
        self.hud_update()
       #Exibe background
        pygame.Surface.blit(self.mapa,self.bg,(self.pos_cam[0],self.pos_cam[1]))

        
        elementos.draw(self.mapa)
        
        hud.draw(self.tela) #desenha o hud
        self.camera_movimenta()
        self.cont_aves = len(aves.sprites())
        self.tela.blit(self.player.txt_live,(50,0.9*HEIGHT))
        self.tela.blit(self.player.txt_score,(50,0.05*HEIGHT))
        self.tela.blit(self.txt_cont_aves,(0.7*WIDTH,0.05*HEIGHT))
        pygame.display.flip()
        return

    

class Chão(pygame.sprite.Sprite): #Classe para iniciar um tile
    def __init__(self, tam = tuple, pos=tuple,img=str, fisica = bool) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.pos = pos
        self.tam = tam
        self.image = pygame.transform.scale(self.image,self.tam)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        if not fisica == False:
            self.add(allgnds)
        self.add(elementos)
    

        return
    

    

        

class Corpo(pygame.sprite.Sprite):
   
   def __init__(self, tam = tuple, pos=tuple,img= pygame.SurfaceType) :
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.tam = tam
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.jump = False
        self.vx = 0
        self.vy = 0
        self.state = IDLE
        self.andar = True
        self.Fall = True
        self.flip= False
        self.add(elementos)
       
        
        
        
    
   
       
        
        

   def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.Fall = True
        self.g = 0.05 #aceleração da gravidade
        if self.vy < 3: #Velocidade maxima de queda
            self.vy += self.g

          #Movimento em y a ser analisado 
        self.proxima_posicao = pygame.Rect.copy(self.rect)
        self.proxima_posicao.y += self.vy
        self.colisao_Y = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.proxima_posicao):
                self.colisao_Y= True
                self.vy = 0
                if gnd.rect.y > self.rect.y : # colisão com limite no chão
                    self.Fall = False
                    self.rect.y= gnd.rect.y - self.rect.height
                if gnd.rect.y < self.rect.y : # colisão com limite no teto
                    self.Fall = True
                    self.rect.top = gnd.rect.bottom 
                
                break
        
        
        # permite o movimento caso não colida

        if not self.colisao_Y:
            self.rect.y = self.proxima_posicao.y

        #Movimento em x a ser analisado 
        self.proxima_posicao = pygame.Rect.copy(self.rect)
        self.proxima_posicao.x +=  self.vx
        self.colisao_X = False
        #confere se ira entrar em um objeto
        for gnd in allgnds:
            if pygame.Rect.colliderect(gnd.rect,self.proxima_posicao):
                self.colisao_X = True
                break
        
        # permite o movimento caso não colida

        if not self.colisao_X:
            self.rect.x = self.proxima_posicao.x

        # confere se não há mais onde cair
        self.passou_all_gnds = True
        for gnd in allgnds:
            if gnd.rect.y > self.rect.y-300:
                self.passou_all_gnds = False 
                break

        # caiu no void --> reposiciona
        if self.passou_all_gnds:
            self.passou_all_gnds = True
        else:
            self.passou_all_gnds = False
        

        #cola a imagem no colisor 
        
        self.rect.center = self.rect.center 

 
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
        self.lives_player_max = self.lives_player
        self.lives_off = 0
        self.score = 0
        
    
        
        
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
        

        if self.passou_all_gnds == True:
            self.lives_player -=1
            self.rect.y = 0
            self.rect.x = 10
        
        self.lives_off = self.lives_player_max - self.lives_player

        self.heart = pygame.font.Font('Assets/-interacoes/Hearts Salad.otf',48)
        self.fonte = pygame.font.Font('Assets\-interacoes\Alfabeto.ttf',48)
        self.txt_live = self.heart.render('N' * self.lives_player + 'M'*self.lives_off, True, (255,0,0))
        self.txt_score = self.fonte.render('{0}'.format(self.score),True, (255,255,255))
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

class Ave(Corpo):
    def __init__(self, pos=tuple):
        img = pygame.image.load("Assets/-bird/-bird (1).png")
        tam= (60,60)
        img= pygame.transform.scale(img,tam)
        Corpo.__init__(self,tam,pos,img)
        self.runtime = random.randint(1000,2000) 
        self.lastupdate = pygame.time.get_ticks() 
        self.vx = - (random.randint(10,20)/10)
        self.pos = pos
        self.animacoes= {}
        self.animacoes["fly"] = []
        self.frametick = 100
        self.frame= 0
        self.last_update = pygame.time.get_ticks()
        self.flip= False
        self.add(aves)

         #Cria lista de frames da animação fly
        for i in range(3,10):
            imgprov = pygame.image.load(f"Assets\-bird\-bird ({i}).png")
            imgprov = pygame.transform.scale(imgprov,self.tam)
            self.animacoes["fly"].append(imgprov)
        self.anim = self.animacoes["fly"]
    def anima(self):
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
        self.image = self.anim[self.frame]
        if self.flip:
            self.image = pygame.transform.flip(self.image,1,0)

        return


    def update(self):
        now = pygame.time.get_ticks()
        self.deltaticks = now - self.lastupdate
        if self.deltaticks >= self.runtime:
            self.lastupdate = now
            self.vx *= -1 #Inverte velocidade
            self.flip = not self.flip

        self.rect.y = self.pos[1]
        self.anima()
        Corpo.update(self)

        return 
        
   
   
class Diamante(pygame.sprite.Sprite):
    def __init__(self, pos = tuple):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Assets/-interacoes/diamante.png.png")
        img = pygame.transform.scale(img,(40,40))
        self.image = img
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.add(elementos)
        self.add(all_diamantes)
