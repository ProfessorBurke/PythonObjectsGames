"""A simple event loop."""
# Import and initialize pygame.
import pygame
pygame.init()

def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Process events by displaying event information."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event

    # Set up assets.
    screen = make_window(SIZE, "Try generating events!")
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Display event information.
            print("{:7s}{}".format("Name: ", pygame.event.event_name(e.type)))
            print("{:7s}{}".format("Type: ", e.type))
            print("{:7s}{}".format("Dict: ", e.__dict__))
            print("*******")
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
