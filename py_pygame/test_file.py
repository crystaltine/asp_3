import pygame
import sys
import random
from key_listener import capture_keypress_loop

pygame.init()

running = True
   
SKY = (97, 120, 232)

width = 1920 # pygame.display.get_desktop_sizes()[0][0]
height = 1080 # pygame.display.get_desktop_sizes()[0][1]

screen = pygame.display.set_mode([width,height])
screen.fill(SKY)
pygame.display.set_caption("Game")
# size = pygame.display.get_desktop_sizes()
grass = pygame.image.load('grasse.png')
grass = pygame.transform.scale(grass, (int(width), int(2 * height/3)))
mtns = pygame.image.load('mtns.png')
mtns = pygame.transform.scale(mtns, (width*2, height/5))
FPS = pygame.time.Clock()
#player = User(Sprite) insert sprite later

#call object instances outside the loop
while running:
    FPS.tick(24) #moved timer into loop
    screen.blit(grass, (0, 2*height/5))
    screen.blit(mtns, (0, height/5))
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    #key numbers for keydowbs binary onkeyevent -> send to server
    #up: 00
    #down: 01
    #left: 10
    #right: 11

    #keydown: 1##
    #keyup: 0##

   
pygame.quit()
sys.exit()
