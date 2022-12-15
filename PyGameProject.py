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

# hockey ball
ball_icon = pygame.image.load('ball.png')
ball_icon = pg.transform.scale(ball_icon, (100, 100))
ballX = 700
ballY = 350
ballspeedX, ballspeedY = 8, 8
ball_rect = pygame.Rect(ballX, ballY, 100, 100)

# moving the ball
def ball():
    global ballY, ballX, ballspeedY, ballspeedX, ball_rect, text1, text2, screen, text1rect, text2rect, log, score1, score2, screen
    if log == 0:
        score1 = score1 - 1
        score2 = score2 - 1
        log = log + 1

    screen.blit(ball_icon, (ballX, ballY))

    if ballY >= 250 and ballY <= 450 and ballX <=20:
        score2 += 1
        underdefault()
    elif ballY >= 250 and ballY <= 450 and ballX >= 1380:
        score1 += 1
        underdefault()
    else:
        ballY += ballspeedY
        if ballY >= 680:
            ballspeedY *= -1
        elif ballY <= 20:
            ballspeedY *= -1
        ballX += ballspeedX
        if ballX >= 1380:
            ballspeedX *= -1
        elif ballX <= 20:
            ballspeedX *= -1

# blue player's characteristics 
player1_icon = pygame.image.load('playerleft.png')
player1_icon = pg.transform.scale(player1_icon, (100, 100))
player1X = 300
player1Y = 350
player1speedx = 0
player1speedy = 0
def player1():
    screen.blit(player1_icon, (player1X, player1Y))

# red player's characteristics
player2_icon = pygame.image.load('playerright.png')
player2_icon = pg.transform.scale(player2_icon, (100, 100))
player2X = 1100
player2Y = 350
player2speedx = 0
player2speedy = 0
def player2():
    screen.blit(player2_icon, (player2X, player2Y))



bool = True
while bool:

    screen.blit(background, (0, 0))
    ball()
    
    
    
    player1()
    player2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bool = False
    

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2speedx = -5
            if event.key == pygame.K_RIGHT:
                player2speedx = 5
            if event.key == pygame.K_UP:
                player2speedy = -5
            if event.key == pygame.K_DOWN:
                player2speedy = 5
            
            if event.key == pygame.K_a:
                player1speedx = -5
            if event.key == pygame.K_d:
                player1speedx = 5
            if event.key == pygame.K_w:
                player1speedy = -5
            if event.key == pygame.K_s:
                player1speedy = 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1speedx = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1speedy = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2speedx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2speedy = 0
            if event.key == pygame.K_SPACE and game:
                print('done')
                ballX = 700
                ballY = 350
                player1X = 300
                player1Y = 350 
                player2X = 1100
                player2Y = 350
                score1 = 0
                score2 = 0
                game = False
        LEFT, RIGHT = 1, 3
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            player2speedy = -5
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            player2speedy = 5
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            player2speedy = 0
        if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
            player2speedy = 0