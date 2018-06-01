#! /usr/bin/env python2.7

import pygame
from pygame.locals import *
import sys
import random
import time
import os
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

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
        self.blackwon = GameSprite(self.screen, 'winner.png', (75, 200))
        self.redwon = GameSprite(self.screen, 'winner.png', (925, 200))
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
        winner = None
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
            tie_checker = 0
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
                    elif self.blackwon.rect.collidepoint(pos) == True:
                        winner = "Black"
                    elif self.redwon.rect.collidepoint(pos) == True:
                        winner = "Red"
                    clicked = False
            self.black.update(0, 0)
            self.red.update(0, 0)
            self.blackwon.update(0, 0)
            self.redwon.update(0, 0)
            self.black.draw()
            self.red.draw()
            self.blackwon.draw()
            self.redwon.draw()
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
                                    grid[i][5] = "BLACK"
                                    break
                                elif grid[i][5] != None and grid[i][4] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][4] = "BLACK"
                                    break
                                elif grid[i][4] != None and grid[i][3] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][3] = "BLACK"
                                    break
                                elif grid[i][3] != None and grid[i][2] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][2] = "BLACK"
                                    break
                                elif grid[i][2] != None and grid[i][1] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][1] = "BLACK"
                                    break
                                elif grid[i][1] != None and grid[i][0] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][0] = "BLACK"
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
                                    grid[i][5] = "RED"
                                    break
                                elif grid[i][5] != None and grid[i][4] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][4] = "RED"
                                    break
                                elif grid[i][4] != None and grid[i][3] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][3] = "RED"
                                    break
                                elif grid[i][3] != None and grid[i][2] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][2] = "RED"
                                    break
                                elif grid[i][2] != None and grid[i][1] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][1] = "RED"
                                    break
                                elif grid[i][1] != None and grid[i][0] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][0] = "RED"
                                    break
                                break
                            break
                    else:
                        continue

            for i in range(0, len(placeBlack)):
                coin = GameSprite(self.screen, "4row_black.png", placeBlack[i])
                coin.rect.centerx = placeBlack[i][0] + 100
                coin.rect.centery = placeBlack[i][1]
                coin.update(5, 0)
                coin.draw()
            for i in range(0, len(placeRed)):
                coin = GameSprite(self.screen, "4row_red.png", placeRed[i])
                coin.rect.centerx = placeRed[i][0] + 100
                coin.rect.centery = placeRed[i][1]
                coin.update(5, 0)
                coin.draw()

            self.screen.blit(self.textsurface, ((self.screen_width / 2) - (self.textsurface.get_rect().width / 2), 20))

            for i in range(0, len(self.blocks)):
                for j in range(0, len(self.blocks[i])):
                    self.blocks[i][j].update(0, 0)
                    self.blocks[i][j].draw()

            pygame.display.flip()

            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    if grid[i][j] != None:
                        tie_checker += 1
                        if tie_checker == 36:
                            self.playerTie(x)

            if winner == "Black":
                self.blackPlayerWon()
            elif winner == "Red":
                self.redPlayerWon()

    def playerTie(self):
        self.acticvated = False
        pygame.display.quit()
        print "_____   ____________    |                              /\                    ==================                                |  "
        print "  |          |        __|                             /  \                            |                                        |  "
        print "  |          |                                       /    \                           |                                        |  "
        print "  |          |                                      /      \                          |         |===|      /==========\        |  "
        print "  |          |              _________              /        \                         |         |===|     /            \       |  "
        print "  |          |             /                      /          \                        |           |      /              \      |  "
        print "  |          |             |                     /            \                       |           |     |================      |  "
        print "  |          |             |                    /==============\                      |           |     |                      |  "
        print "  |          |             \________           /                \                     |           |     |                      |  "
        print "  |          |                      \         /                  \                    |           |     |                      |  "
        print "  |          |                      |        /                    \                   |           |     \                 /    |  "
        print "  |          |                      |       /                      \                  |           |      \               /   |===|"
        print "__|__        |              ________/      /                        \                 |           |       \_____________/    |===|"

    def redPlayerWon(self):
        self.acticvated = False
        pygame.display.quit()
        print "|  /=======\                  |------------          |=\                          ________________                                                "
        print "| /         \                 |                      | =\                        /                \              |            /|    |------------ "
        print "|/           \                |                      |  =\                      /                  \             |           / |    |             "
        print "|             \               |                      |   =\                    /                    \            |          /  |    |             "
        print "|==============               |                      |    =\                  |                      |           |         /   |    |             "
        print "|             \               |                      |     =\                 |                      |           |        /    |    |             "
        print "|              \              |                      |      =\                |                      |           |       /     |    |             "
        print "|               \             |-----------           |      =/                |                      |           |      /      |    |------------ "
        print "|                \            |                      |     =/                 |                      |           |     /       |    |             "
        print "|                 \           |                      |    =/                   \                    /            |    /        |    |             "
        print "|                  \          |                      |   =/                     \                  /             |   /         |    |             "
        print "|                   \         |                      |  =/                       \                /              |  /          |    |             "
        print "|                    \        |                      | =/                         \              /               | /           |    |             "
        print "|                     \       |------------          |=/                           \____________/                |/            |    |-------------"

        print "\n If You'd Like To Play Again, Click Up, Then Enter"

    def blackPlayerWon(self):
        self.acticvated = False
        pygame.display.quit()
        print "|--------           |                            /\                      |----\        |      /            /|        "
        print "|        \          |                           /  \                     |     \       |     /            / |        "
        print "|         \         |                          /    \                    |      \      |    /            /  |        "
        print "|          \        |                         /      \                   |             |   /                |        "
        print "|           /       |                        /        \                  |             |  /                 |        "
        print "|------------       |                       /----------\                 |             |-/                  |        "
        print "|           \       |                      /            \                |             |-\                  |        "
        print "|          /        |                     /              \               |             |  \                 |        "
        print "|         /         |                    /                \              |             |   \                |        "
        print "|        /          |                   /                  \             |      /      |    \               |        "
        print "|       /           |                  /                    \            |     /       |     \              |        "
        print "|------/            |_____________    /                      \           |----/        |      \     ________|________"

        print "\n If You'd Like To Play Again, Click Up, Then Enter"

os.system('clear')
play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (Yepper Pepper/Noper Doper): ")
if play == "Yepper Pepper":
    print "Rules:"
    time.sleep(1)
    print "* Decide Amougnst Yourselves Who Gets Black And Who Gets Red."
    time.sleep(1)
    print "* Who Ever Is Up, Click On Your Coin, Then Click On THe Arrow That You Want The Column To Be In."
    time.sleep(1)
    print "* The Next Player Goes, And So On"
    time.sleep(1)
    print "* Who Wins, May Claim Their Trophy By Clicking On It, Then Look Back To This Terminal Window."
    time.sleep(1)
    ok = raw_input("OK? (Yepper Pepper/Noper Doper): ")
    if ok == "Yepper Pepper":
        game = connectFour(1000, 800)
        game.run(True)
    else:
        sys.exit(0)
elif play == "Noper Doper":
    sys.exit(0)
else:
    sys.exit(1)
