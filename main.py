import math
import sys

import pygame

import classes

#create grid map 1200x1200
map = [[0 for x in range(1000)] for y in range(1000)]

# create the player
player1 = classes.Player('player1', 'player1', [500, 500])

#create cars
car1 = classes.Car('car1', 'car1',pygame.transform.rotate(pygame.image.load("assets/FerociousGTO-GTAL69-variant1.webp"),-90), [100, 100])

player1.car = car1

#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Map')

# load map image
mapImg = pygame.image.load('map.webp')
# get the dimensions of the image
image_width = mapImg.get_width()
image_height = mapImg.get_height()


# set the position of the image in the window
image_x = (WINDOWWIDTH - image_width) // 2
image_y = (WINDOWHEIGHT - image_height) // 2

# field of view
fov = 100


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    # move the player
    if pygame.key.get_pressed()[pygame.K_UP]:
        player1.move('up')
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        player1.move('down')
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        player1.move('left')
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        player1.move('right')
    # clear the screen
    windowSurface.fill((255, 255, 255))
    cropx, cropy = player1.x-fov/2, player1.y-fov/2
    # Change value to crop different rect areas
    cropRect = (cropx, cropy, fov, fov)
    # create portion of image
    mapImg2 = mapImg.subsurface(cropRect)
    # scale the portion of image to fit the entire window
    mapImg2 = pygame.transform.scale(mapImg2, (WINDOWWIDTH, WINDOWHEIGHT))
    # draw the visible portion of the image to the visible surface
    windowSurface.blit(mapImg2, (0, 0))

    # draw the player
    #print(player1.x, player1.y)
    # draw the player car
    windowSurface.blit(player1.car.image, (250,250))

    pygame.display.update()
    mainClock.tick(40)
