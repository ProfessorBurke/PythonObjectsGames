"""Handle mouse events by drawing and erasing."""

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
    """Process mouse events by drawing and clearing."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    brush: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Move mouse to draw, click to clear"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.Surface((SIZE, SIZE))
    background.fill((255, 255, 255))
    brush = pygame.Surface((10, 10))
    brush.fill((0, 0, 255))
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
                background.blit(brush, e.__dict__["pos"])
            elif e.type == pygame.MOUSEBUTTONDOWN:
                background.fill((255, 255, 255))
                    
        # Draw the background.
        screen.blit(background, (0, 0))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
