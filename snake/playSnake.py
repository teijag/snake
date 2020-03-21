import pygame
import sys
import random
from pygame.locals import *
import time

# initialize pygame
pygame.init()

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640,480))

pygame.display.set_caption('Snake')

image = pygame.image.load('game.ico')

pygame.display.set_icon(image)

# color scheme
redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)
lightColor = pygame.Color(220, 220, 220)


