import pygame
from pygame.locals import *
import sys # Imports the System Module
import random
import time

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
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza")
        self.black = GameSprite(self.screen, '4row_black.png', (150,550))
        self.red = GameSprite(self.screen, '4row_red.png', (750,550))

    def run(self, running):
        pygame.init()
        clock = pygame.time.Clock()

        while running == True:
            clock.tick(30)
            for event in pygame.event.get():
                if not hasattr(event, 'key'): # if its not a key event then ignore it
                    continue
            print "Connect4 Game Running At " + str(clock.get_fps()) + " FPS"
            self.screen.fill((0, 255, 255))
            self.black.update(0, 0)
            self.red.update(0, 0)
            self.black.draw()
            self.red.draw()
            pygame.display.flip()

play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (y/n): ")
if play == "y":
    game = connectFour(900, 700)
    game.run(True)
elif play == "n":
    sys.exit(0)
else:
    sys.exit(1)
