import pygame
WIDTH = 600
HEIGHT = 600


START_POSITION = (250, 550, 100, 50)    

BASE_RADIUS = 30    

BASE_FONT_SIZE = 36 



BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
