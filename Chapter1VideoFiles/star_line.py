"""Draw firework stars with pygame."""

import pygame

# Define some size constants to make drawing easier.
SIZE: int = 480

# Annotate variables
screen: pygame.Surface
star: pygame.Surface
star_num: int
x: float
y: float

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Stars!")

# Load the star image.
star = pygame.image.load("red_star.png")

# Draw ten stars in a horizontal line.
star_num = 0
x = 100
y = 100
while star_num < 10:
    screen.blit(star, (x,y))
    x += 20
    star_num += 1

# Show the drawing.
pygame.display.flip()

# Quit when the user presses enter.
input("Press enter to quit...")
pygame.quit()
