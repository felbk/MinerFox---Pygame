# Falta fazer.
import pygame
from pygame.locals import *
from sys import exit
from Config import WIDTH, HEIGHT

def load_assets():
    assets = {}
    assets['tela_inicial'] = pygame.image.load('Assets/-tela_final/-tela_final.jpg').convert()
    assets['tela_inicial'] = pygame.transform.scale(assets['tela_inicial'],(WIDTH,HEIGHT))
    assets['start_text'] = pygame.font.Font('Assets/-interacoes/Alfabeto.ttf',35)
    assets['text_restart'] = assets['start_text'].render('Press Enter to Restart',True,(255,255,255))
    assets['text_esc'] = assets['start_text'].render('Press Esc to Exit', True, (255,255,255))
    return assets