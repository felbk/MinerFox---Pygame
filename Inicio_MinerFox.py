import pygame

from Config import WIDTH, HEIGHT
from os import path

def inicio_minerfox(tela):
    pygame.time.Clock()
    tela_inicial = pygame.image.load('Assets/-tela_inicial/-tela_inicio_Miner_Fox.jpg').convert()
    tela_inicial = pygame.transform.scale(tela_inicial,(WIDTH,HEIGHT))
    tela_inicial_rect = tela_inicial.get_rect()

    working = True
    while working: