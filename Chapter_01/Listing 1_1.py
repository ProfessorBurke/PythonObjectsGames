"""Hello world! in Python and pygame."""

# Import and initialize pygame.
import pygame
pygame.init()

# Annotate variable
screen: pygame.Surface

# Display "Hello world!" as the window title.
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Hello world!")

# Display "Hello world!" in the console.
print("Hello world!")

# Quit when the user presses enter.
input("Press enter to quit...")
pygame.quit()
