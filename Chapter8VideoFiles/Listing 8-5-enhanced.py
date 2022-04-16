"""Illustrate centering and boundary checking."""

# Import and initialize pygame.
import pygame
pygame.init()

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Draw an image centered and at the boundaries."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    SQUARE_SIZE: int = 50
    screen: pygame.Surface
    background: pygame.Surface
    square: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Boundary Demo")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((255, 255, 255))
    square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    square.fill((0, 150, 150))
    clock: pygame.time.Clock = pygame.time.Clock()

    # Calculate coordinate to blit square to center of background.
    center_xcoord: float = (background.get_width() / 2) - (square.get_width() / 2)
    center_ycoord: float = (background.get_height() / 2) - (square.get_height() / 2)

    # Calculate coordinate to blit square to the bottom, right.
    bottom_right_xcoord: float = background.get_width() - square.get_width()
    bottom_right_ycoord: float = background.get_height() - square.get_height()
    
    # Blit square to upper left.
    background.blit(square, (0, 0))

    # Draw to the screen and show.
    background.blit(square, (center_xcoord, center_ycoord))
    background.blit(square, (bottom_right_xcoord, bottom_right_ycoord))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                       
    pygame.quit()

main()
