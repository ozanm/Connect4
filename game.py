import pygame
from pygame.locals import *
import sys # Imports the System Module
window_width = 1000
window_height = 650
window_size = window_width, window_height
screen = pygame.display.set_mode(window_size)
red_circle = None
black_circle = None
screen_color = (0, 0, 255)
screen.fill(screen_color)
