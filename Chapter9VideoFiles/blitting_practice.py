"""Add the program description here."""

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
    """Add a function description."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"
    x: int = 0
    y: int = 200

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.Surface((SIZE, SIZE))
    ball: pygame.Surface = pygame.image.load("ball.gif").convert()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEMOTION:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif e.type == pygame.MOUSEBUTTONUP:
                pass
            elif e.type == pygame.KEYDOWN:
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw the background.
        x += 5
        screen.blit(background, (0, 0))
        screen.blit(ball, (x, y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
