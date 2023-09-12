# Import and initialize pygame
import pygame
pygame.init()

# Canvas settings and variables
SCREEN_SIZE = (700, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Draw stickman function
def draw_stickman(color, x, y) :
    #head
    pygame.draw.circle(screen, color, (x + 80, y + 80), 50, 3)
    #body
    pygame.draw.line(screen, color, (x + 80, y + 130), (300, 350), 3)
    #arms
    pygame.draw.line(screen, color, (300, 240), (230, 300), 3)
    pygame.draw.line(screen, color, (300, 240), (360, 300), 3)
    #legs
    pygame.draw.line(screen, color, (300, 350), (260, 430), 3)
    pygame.draw.line(screen, color, (300, 350), (340, 430), 3)


# Open canvas
run = True
while run:
    #open to empty white screen
    screen.fill("white")

    #draw shapes
    draw_stickman("black") # complete other coords

    for event in pygame.event.get(): 
        #when user clicks X on window so the window isnt stuck open
        if event.type == pygame.QUIT:
            run = False

    #update canvas with whats been drawn 
    pygame.display.flip()