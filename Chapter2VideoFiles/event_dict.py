"""Show the event dictionary for events of different types."""

import pygame

def main() -> None:
    """The main event loop.  Handle clicks until the user quits."""
    # Define constants and annotate variables
    SIZE: int = 480
    screen: pygame.Surface
    user_quit: bool
    event: pygame.event.Event

    # Create a pygame window.
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Try pressing keys and moving the mouse")

    # Wait for the user to quit.
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            # Display event information.
            print("Event type: " + str(event.type))
            print("Event dict: " + str(event.__dict__))
            if event.type == pygame.QUIT:
                user_quit = True

    pygame.quit()

main()
