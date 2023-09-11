# Import and initialize pygame
import pygame
pygame.init()

# Canvas settings and variables
SCREEN_SIZE = (700, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Open canvas
run = True
while run:
    #open to empty white screen
    screen.fill("white")

    #draw shapes

    
    for event in pygame.event.get(): 
        #when user clicks X on window so the window isnt stuck open lol
        if event.type == pygame.QUIT:
            run = False

    #update canvas with whats been drawn 
    pygame.display.flip()