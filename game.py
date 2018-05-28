#! /usr/bin/env python2.7

import pygame
from pygame.locals import *
import sys # Imports the System Module
import random
import time
import os

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
        self.acticvated = True
        self.lobster = pygame.font.Font('Lobster-Regular.ttf', 40)
        self.textsurface = self.lobster.render("THIS PROJECT IS BETTER THAN THE OTHERS", False, (255, 69, 0))
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza FPS: 30")
        self.black = GameSprite(self.screen, '4row_black.png', (75,700))
        self.red = GameSprite(self.screen, '4row_red.png', (925,700))
        self.arrows =  [GameSprite(self.screen, "Black_Down_Arrow.png", (245, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (345, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (445, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (545, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (645, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (745, 100))]
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
        aboutToPickRow = False
        clicked = False
        placeBlack = []
        placeRed = []
        grid = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
        for i in range(0, len(self.blocks)):
            for j in range(0, len(self.blocks[i])):
                self.blocks[i][j] = GameSprite(self.screen, '4row_board.png', ((i * 100) + 250, (j * 100) + 200))

        while running == True and self.acticvated == True:
            clock.tick(30)
            pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza FPS: " + str(clock.get_fps()))
            self.screen.fill((0, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                #elif not hasattr(event, 'key'): # if its not a key event then ignore it
                    #continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    pos = pygame.mouse.get_pos()
                    if blackisup == True and self.black.rect.collidepoint(pos) == True:
                        self.textsurface = self.lobster.render("Now Click On The Arrow That You Want The Coin To Fall In!", False, (255, 69, 0))
                        aboutToPickRow = True
                    elif blackisup == False and self.red.rect.collidepoint(pos) == True:
                        self.textsurface = self.lobster.render("Now Click On The Arrow That You Want The Coin To Fall In!", False, (255, 69, 0))
                        aboutToPickRow = True
                    clicked = False
            self.black.update(0, 0)
            self.red.update(0, 0)
            self.black.draw()
            self.red.draw()
            if aboutToPickRow == True:
                for i in range(0, len(self.arrows)):
                    self.arrows[i].update(0, 0)
                    self.arrows[i].draw()
                for i in range(0, len(self.arrows)):
                    if self.arrows[i].rect.collidepoint(pos) == True:
                        if blackisup == True:
                            for j in range(0, len(grid)):
                                if grid[i][5] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][5].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][5] = 1
                                    break
                                elif grid[i][5] == 1 and grid[i][4] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][4] = 1
                                    break
                                elif grid[i][4] == 1 and grid[i][3] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][3] = 1
                                    break
                                elif grid[i][3] == 1 and grid[i][2] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][2] = 1
                                    break
                                elif grid[i][2] == 1 and grid[i][1] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][1] = 1
                                    break
                                elif grid[i][1] == 1 and grid[i][0] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][0] = 1
                                    break
                                break
                            break
                        elif blackisup == False:
                            for j in range(0, len(grid)):
                                if grid[i][5] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][5].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][5] = 1
                                    break
                                elif grid[i][5] == 1 and grid[i][4] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][4] = 1
                                    break
                                elif grid[i][4] == 1 and grid[i][3] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][3] = 1
                                    break
                                elif grid[i][3] == 1 and grid[i][2] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][2] = 1
                                    break
                                elif grid[i][2] == 1 and grid[i][1] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][1] = 1
                                    break
                                elif grid[i][1] == 1 and grid[i][0] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][0] = 1
                                    break
                                break
                            break
                    else:
                        continue

            for i in range(0, len(placeBlack)):
                coin = GameSprite(self.screen, "4row_black.png", placeBlack[i])
                coin.rect.centerx = placeBlack[i][0] + 100
                coin.rect.centery = placeBlack[i][1]
                coin.update(10, 0)
                coin.draw()
            for i in range(0, len(placeRed)):
                coin = GameSprite(self.screen, "4row_red.png", placeRed[i])
                coin.rect.centerx = placeRed[i][0] + 100
                coin.rect.centery = placeRed[i][1]
                coin.update(10, 0)
                coin.draw()

            self.screen.blit(self.textsurface, ((self.screen_width / 2) - (self.textsurface.get_rect().width / 2), 20))

            for i in range(0, len(self.blocks)):
                for j in range(0, len(self.blocks[i])):
                    self.blocks[i][j].update(0, 0)
                    self.blocks[i][j].draw()

            if not grid[0][0] == None:
                if not grid[0][1] == None:
                    if not grid[0][2] == None:
                        if not grid[0][3] == None:
                            if not grid[0][4] == None:
                                if not grid[0][5] == None:
                                    if not grid[1][0] == None:
                                        if not grid[1][1] == None:
                                            if not grid[1][2] == None:
                                                if not grid[1][3] == None:
                                                    if not grid[1][4] == None:
                                                        if not grid[1][5] == None:
                                                            if not grid[2][0] == None:
                                                                if not grid[2][1] == None:
                                                                    if not grid[2][2] == None:
                                                                         if not grid[2][3] == None:
                                                                             if not grid[2][4] == None:
                                                                                 if not grid[2][5] == None:
                                                                                     if not grid[3][0] == None:
                                                                                         if not grid[3][1] == None:
                                                                                             if not grid[3][2] == None:
                                                                                                 if not grid[3][3] == None:
                                                                                                     if not grid[3][4] == None:
                                                                                                         if not grid[3][5] == None:
                                                                                                             if not grid[4][0] == None:
                                                                                                                 if not grid[4][1] == None:
                                                                                                                     if not grid[4][2] == None:
                                                                                                                         if not grid[4][3] == None:
                                                                                                                             if not grid[4][4] == None:
                                                                                                                                 if not grid[4][5] == None:
                                                                                                                                     if not grid[5][0] == None:
                                                                                                                                         if not grid[5][1] == None:
                                                                                                                                             if not grid[5][2] == None:
                                                                                                                                                 if not grid[5][3] == None:
                                                                                                                                                     if not grid[5][4] == None:
                                                                                                                                                         if not grid[5][5] == None:
                                                                                                                                                             self.playerTie()
            pygame.display.flip()

    def playerTie(self):
        self.acticvated = False
        pygame.display.quit()
        print "_____   ____________    |                              /\                    ==================                                |"
        print "  |          |        __|                             /  \                            |                                        |"
        print "  |          |                                       /    \                           |                                        |"
        print "  |          |                                      /      \                          |         |===|      /==========\        |"
        print "  |          |              _________              /        \                         |         |===|     /            \       |"
        print "  |          |             /                      /          \                        |           |      /              \      |"
        print "  |          |             |                     /            \                       |           |     |================      |"
        print "  |          |             |                    /==============\                      |           |     |                      |"
        print "  |          |             \________           /                \                     |           |     |                      |"
        print "  |          |                      \         /                  \                    |           |     |                      |"
        print "  |          |                      |        /                    \                   |           |     \                 /    |"
        print "  |          |                      |       /                      \                  |           |      \               /   |===|"
        print "__|__        |              ________/      /                        \                 |           |       \_____________/    |===|"

    #def redPlayerWon(self): (METHODS TO CALL AND DEFINE LATER) def blackPlayerWon(self):

os.system('clear')
play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (y/n): ")
if play == "y":
    game = connectFour(1000, 800)
    game.run(True)
elif play == "n":
    sys.exit(0)
else:
    sys.exit(1)
