import pygame
from pygame.locals import *
import sys # Imports the System Module
import random

class GameSprite(pygame.sprite.Sprite):

  def __init__(self, screen, filename, position):
    pygame.sprite.Sprite.__init__(self) # call the parent (Sprite) constructor
    self.screen = screen
    self.image = pygame.image.load(filename)
    self.position = position
    self.rect = self.image.get_rect() # the image's rectangle

  def update(self, dx, dy):
    x, y = self.position
    x += dx
    y += dy
    self.position = (x, y)
    self.rect = self.image.get_rect()
    self.rect.center = self.position # set new position of sprite

  def draw(self):
    self.screen.blit(self.image, self.rect)

class connectFour():
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza")

    def run(self):
        clock = pygame.time.Clock()


while True:
    play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (y/n): ")
    if play == "y":
        game = connectFour(1000, 500)
        game.run()
    elif play == "n":
        sys.exit(0)
