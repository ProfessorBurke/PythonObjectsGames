"""Draw firework stars with pygame."""

import math

# Import and initialize pygame.
import pygame
pygame.init()

# Define some size constants to make drawing easier.
PI_OVER_4: float = math.radians(45)
RADIUS: int = 120
SIZE: int = 480
CENTER: float = (SIZE - 40) / 2

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
star = pygame.image.load("star.png")

# Draw eight stars at 45° angles.
for star_num in range(8):
    # Compute the x and y coordinates of a star.
    x = CENTER + RADIUS * math.cos(star_num * PI_OVER_4)
    y = CENTER + RADIUS * math.sin(star_num * PI_OVER_4)
    
    # Add the star to the drawing.
    screen.blit(star, (x,y))

# Show the drawing.
pygame.display.flip()

# Quit when the user presses enter.
input("Press enter to quit...")
pygame.quit()

            
