# Import and initialize pygame
import pygame
pygame.init()

# Canvas settings and variables
SCREEN_SIZE = (900, 700)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Draw graphics functions
def draw_stickman(color, x, y) :
    #head
    pygame.draw.circle(screen, color, (x + 20, y + 20), 20, 3)
    #body
    pygame.draw.line(screen, color, (x + 20, y + 40), (x + 20, y + 80), 3)
    #arms
    pygame.draw.line(screen, color, (x + 20, y + 50), (x, y + 70), 3)
    pygame.draw.line(screen, color, (x + 20, y + 50), (x + 40, y + 70), 3)
    #legs
    pygame.draw.line(screen, color, (x + 20, y + 80), (x, y + 110), 3)
    pygame.draw.line(screen, color, (x + 20, y + 80), (x + 40, y + 110), 3)
    #face
    pygame.draw.arc(screen, color, (x + 10, y + 20, 20 ,10), 3.14, 0, width = 3)
    pygame.draw.circle(screen, color, (x + 10, y + 20), 3)
    pygame.draw.circle(screen, color, (x + 30, y + 20), 3)

def draw_platform(color, color2, x, y, width, height) :
    #bottom
    pygame.draw.line(screen, color2, (x, y + 8), (x + width, y + 8), height)
    #top
    pygame.draw.line(screen, color, (x, y), (x + width, y), 6)
    


# Open canvas
run = True
while run:
    #open to empty white screen
    screen.fill("white")

    #draw shapes
    draw_stickman("darkorchid", 600, 500)

    for event in pygame.event.get(): 
        #when user clicks X on window so the window isnt stuck open
        if event.type == pygame.QUIT:
            run = False

    #update canvas with whats been drawn 
    pygame.display.flip()