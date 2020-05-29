import pygame, sys

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size, flags = pygame.DOUBLEBUF)
pygame.display.set_caption("Video")

background = pygame.Surface(size)
screen.blit(background, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.flip()