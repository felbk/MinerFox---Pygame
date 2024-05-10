
import pygame
from pygame.locals import *
from sys import exit


FPS = 30

pygame.init()
pygame.time.Clock().tick(FPS)

WIDTH = pygame.display.get_desktop_sizes()[0][0]
HEIGHT = pygame.display.get_desktop_sizes()[0][1]