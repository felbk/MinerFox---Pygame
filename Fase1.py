

def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS

    fase1 = Fase(tela,(2000,2000)) #Cria fase


#função cria blocos do mapa
def posicao_mapa(matriz_mapa,tamanho):
    posicoes = []
    for linha in range(len(matriz_mapa)):
        for coluna in range(len(matriz_mapa[linha])):
        posicao = (coluna, linha*tamanho)
        posicoes.append(posicao)
    return posicoes


#Cria os blocos do chão 
    Chão((tela.get_width(),50),(800,fase1.mapa.get_height() - 50 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,120),(0,fase1.mapa.get_height() - 120 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,50),(500,fase1.mapa.get_height() - 320 ),"Assets\provisorios\chao.png")

    while fase1.play:
        fase1.update() # Atualiza fase
        
    elementos.empty()
    return {"state": 0 , "fase": 1}


#==============IMPORTS===============

import pygame
from pygame.locals import *
from sys import exit
from sprites import *
from setup import QUIT , PLAYING , HOME


#carregando sons do jogo
pygame.mixer.music.load("songs\som__de_fundo.wav")
pygame.mixer.music.set_volume(0.4)
coleta_diamantes = pygame.mixer.Sound('songs\coleta_diamantes.mp3')
game_over_cacador = pygame.mixer.Sound('songs\game_over_cacador.wav')
game_over_jogo = pygame.mixer.Sound("songs\game_over.mp3")
som_aguia = pygame.mixer.Sound('songs\som_aguia.mp3')
som_cacador = pygame.mixer.Sound('songs\som_cacador.mp3')


