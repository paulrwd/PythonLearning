import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Window")
black = (0,0,0)
blue = (0,0,205)
done = False
x = 0

while not done:
    x += 1
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done  = True

    pygame.draw.rect(window,blue,(300 / x, 20*x ,100 + x , 10 * x))
    pygame.display.flip()

pygame.quit()

