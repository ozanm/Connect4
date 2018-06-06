import pygame
from pygame.locals import *

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
