"""Create a window and add stars when the user clicks."""

import pygame

# Define constants and annotate variables
SIZE: int = 480
screen: pygame.Surface
user_quit: bool
event: pygame.event.Event
star: pygame.Surface
x: int = 10
y: int = 10

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Click the close box to quit!")

# Load the star image.
star = pygame.image.load("red_star.png")

# Process events until quit.
user_quit = False
while not user_quit:
    for event in pygame.event.get():
        # Process a quit choice.
        if event.type == pygame.QUIT:
            user_quit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.blit(star, (x,y))
            x += 20
            if x > SIZE:
                x = 10
                y += 20

    pygame.display.flip()

pygame.quit()
            
