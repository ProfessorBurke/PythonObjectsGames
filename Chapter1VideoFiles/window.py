"""Draw an image in a window."""

import pygame

# Annotate variables
WIDTH: int = 400
HEIGHT: int = 200
screen: pygame.Surface
star: pygame.Surface

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing!")

# Create a star and blit to the screen.
star = pygame.image.load("red_star.png")
screen.blit(star, (0,0))
screen.blit(star, (WIDTH - star.get_width(), HEIGHT - star.get_height()))
pygame.display.flip()

# Wait for the user to press a key.
input("Press enter to quit...")
pygame.quit()
