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
        pygame.init()
        self.lobster = pygame.font.Font('Lobster-Regular.ttf', 40)
        self.textsurface = self.lobster.render("THIS PROJECT IS BETTER THAN THE OTHERS", False, (255, 69, 0))
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza")
        self.black = GameSprite(self.screen, '4row_black.png', (75,700))
        self.red = GameSprite(self.screen, '4row_red.png', (925,700))
        self.arrows =  [GameSprite(self.screen, "down.png", (255, 255)),
                        GameSprite(self.screen, "down.png", (255, 255)),
                        GameSprite(self.screen, "down.png", (255, 255)),
                        GameSprite(self.screen, "down.png", (255, 255)),
                        GameSprite(self.screen, "down.png", (255, 255)),
                        GameSprite(self.screen, "down.png", (255, 255))]
        self.blocks = [[None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None]]

    def run(self, running):
        clock = pygame.time.Clock()
        up = ["Black Is Up!", "Red Is Up!"]
        blackisup = True
        self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
        for i in range(0, len(self.blocks)):
            for j in range(0, len(self.blocks[i])):
                self.blocks[i][j] = GameSprite(self.screen, '4row_board.png', ((i * 100) + 250, (j * 100) + 200))

        while running == True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                #elif not hasattr(event, 'key'): # if its not a key event then ignore it
                    #continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if blackisup == True and self.black.rect.collidepoint(pos) == True:
                        self.textsurface = self.lobster.render("Now Click On The Row That You Want The Coin To Fall In!", False, (255, 69, 0))
                        for i in range(0, len(self.arrows)):
                            self.arrows[i].update(0, 0)
                            self.arrows[i].draw()
                    elif blackisup == False and self.red.rect.collidepoint(pos) == True:
                         self.textsurface = self.lobster.render("Now Click On The Row That You Want The Coin To Fall In!", False, (255, 69, 0))
            print "Connect4 Game By Mikey Jacobs And Ozan Mirza Running At " + str(clock.get_fps()) + " FPS"
            self.screen.fill((0, 255, 255))
            self.black.update(0, 0)
            self.red.update(0, 0)
            self.black.draw()
            self.red.draw()
            self.screen.blit(self.textsurface, ((self.screen_width / 2) - (self.textsurface.get_rect().width / 2), 20))

            for i in range(0, len(self.blocks)):
                for j in range(0, len(self.blocks[i])):
                    self.blocks[i][j].update(0, 0)
                    self.blocks[i][j].draw()

            pygame.display.flip()

play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (y/n): ")
if play == "y":
    game = connectFour(1000, 800)
    game.run(True)
elif play == "n":
    sys.exit(0)
else:
    sys.exit(1)
