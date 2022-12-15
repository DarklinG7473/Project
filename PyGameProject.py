import pygame
import random
import sys
import pygame as pg
from PIL import Image, ImageDraw
from pygame import mixer
from pygame.locals import *
from win32api import GetSystemMetrics


# pygame initializing
pygame.init()
mixer.init()

# main screen
screen = pygame.display.set_mode((1500, 826))
background = pygame.image.load('hockey.jpg')
pygame.display.set_caption('Air Hockey')

# icon of the main screen
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)




bool = True
while bool:

    screen.blit(background, (0, 0))
    ball()
    
    
    
    player1()
    player2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bool = False