# Falta fazer.
import pygame
from pygame.locals import *
from sys import exit
from Config import WIDTH, HEIGHT

def load_assets():
    assets = {}
    #Assets Game Over
    assets['tela_perda'] = pygame.image.load('Assets/-tela_final/-tela_final.jpg').convert()
    assets['tela_perda'] = pygame.transform.scale(assets['tela_perda'],(WIDTH,HEIGHT))
    assets['start_text_perda'] = pygame.font.Font('Assets/-interacoes/Alfabeto.ttf',35)
    assets['text_restart'] = assets['start_text_perda'].render('Press Enter to Restart',True,(255,255,255))
    assets['text_esc'] = assets['start_text_perda'].render('Press Esc to Exit', True, (255,255,255))

    #Assets Tela Inicial
    assets['tela_inicial'] = pygame.image.load('Assets/-tela_inicial/-tela_inicio_Miner_Fox (2).jpg').convert()
    assets['tela_inicial'] = pygame.transform.scale(assets['tela_inicial'],(WIDTH,HEIGHT))
    assets['start_text_inicial'] = pygame.font.Font('Assets/-interacoes/Alfabeto.ttf',46)
    assets['text'] = assets['start_text_inicial'].render('Press Enter to Play',True,(255,255,255))
    
    #Assets Musicas do Jogo
    assets['coleta_diamantes'] = pygame.mixer.Sound('songs\coleta_diamantes.mp3')
    assets['game_over_cacador'] = pygame.mixer.Sound('songs\game_over_cacador.wav')
    assets['game_over_jogo'] =pygame.mixer.Sound("songs\game_over.mp3")
    assets['som_aguia'] = pygame.mixer.Sound('songs\som_aguia.mp3')
    assets['som_cacador'] = pygame.mixer.Sound('songs\som_cacador.mp3')
    return assets