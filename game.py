import pygame
from pygame.locals import *
import sys # Imports the System Module
import random
class GameSprite(pygame.sprite.Sprite):
  """ This class represents a sprite. It derives from the "Sprite"
      class in Pygame.
  """

  def __init__(self, screen, filename, position):
    """ Constructor. Pass in the screen, the name of image file to open,
        and its starting position (x, y). 
    """
    pygame.sprite.Sprite.__init__(self) # call the parent (Sprite) constructor
    self.screen = screen
    self.image = pygame.image.load(filename)
    self.position = position
    self.rect = self.image.get_rect() # the image's rectangle
   
  def update(self, dx, dy):
    """ Update the sprite's position """
    x, y = self.position
    x += dx
    y += dy
    self.position = (x, y)
    self.rect = self.image.get_rect()
    self.rect.center = self.position # set new position of sprite

  def draw(self):
    """ Draw the sprite on the screen """
    self.screen.blit(self.image, self.rect)
          
