# Import and initialize pygame
import pygame
pygame.init()

# Canvas settings and variables
SCREEN_SIZE = (900, 700)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Draw stickman function
def draw_stickman(color, x, y) : #(230, 100)
    #head
    pygame.draw.circle(screen, color, (x + 70, y + 80), 50, 3)
    #body
    pygame.draw.line(screen, color, (x + 70, y + 130), (x + 70, y + 250), 3)
    #arms
    pygame.draw.line(screen, color, (x + 70, y + 140), (x, y + 200), 3)
    pygame.draw.line(screen, color, (x + 70, y + 140), (x + 130, y + 200), 3)
    #legs
    pygame.draw.line(screen, color, (x + 70, y + 250), (x + 30, y + 330), 3)
    pygame.draw.line(screen, color, (x + 70, y + 250), (x + 110, y + 330), 3)
    #face
    pygame.draw.arc(screen, color, (x + 45, y + 60, 50 ,50), 3.14, 0, width = 3)
    pygame.draw.circle(screen, color, (x + 50, y + 70), 5)
    pygame.draw.circle(screen, color, (x + 90, y + 70), 5)

def draw_platform(start, end, w, color, color2) :
    #top
    pygame.draw.line(screen, color, start, end, w)



# Open canvas
run = True
while run:
    #open to empty white screen
    screen.fill("white")

    #draw shapes


    for event in pygame.event.get(): 
        #when user clicks X on window so the window isnt stuck open
        if event.type == pygame.QUIT:
            run = False

    #update canvas with whats been drawn 
    pygame.display.flip()