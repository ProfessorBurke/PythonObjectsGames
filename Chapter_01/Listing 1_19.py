"""Draw a star at a random location for each user click."""

import random

# Import and initialize pygame.
import pygame
pygame.init()

# Define constants and annotate variables
SIZE: int = 480
screen: pygame.Surface
star: pygame.Surface
offset_w: float
offset_h: float
user_quit: bool
event: pygame.event.Event
x: int
y: int

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Click to make a star!")

# Load the star image.
star = pygame.image.load("star.png")
offset_w = star.get_width() / 2
offset_h = star.get_height() / 2

# Draw a star for each click.
user_quit = False
while not user_quit:
    for event in pygame.event.get():
        # Process a quit choice.
        if event.type == pygame.QUIT:
            user_quit = True
        # Process a click by drawing a star.
        elif event.type == pygame.MOUSEBUTTONUP:
            x = random.randint(0,SIZE) - offset_w
            y = random.randint(0,SIZE) - offset_h
            screen.blit(star, (x,y))   
    # Show the drawing.
    pygame.display.flip()

pygame.quit()
            
