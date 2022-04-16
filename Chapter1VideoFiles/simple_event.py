"""Create a window and wait for the user to close it."""

import pygame

# Define constants and annotate variables
SIZE: int = 480
screen: pygame.Surface
user_quit: bool
event: pygame.event.Event

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Click the close box to quit!")

# Wait for the user to quit.
user_quit = False
while not user_quit:
    for event in pygame.event.get():
        # Process a quit choice.
        if event.type == pygame.QUIT:
            user_quit = True

pygame.quit()
            
