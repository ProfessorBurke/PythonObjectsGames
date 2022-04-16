"""Add the program description here."""

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
    """Add a function description."""
    # Annotate and initialize variables
    WIDTH: int = 640
    HEIGHT: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"
    x: int = 0
    y: int = 200
    dx: int = 5

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background = pygame.Surface((WIDTH, HEIGHT))
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
        # Bouncing code
##        x += dx
##        if x + ball.get_width() > screen.get_width():
##            x = screen.get_width() - ball.get_width()
##            dx *= -1
##        screen.blit(background, (0, 0))
##        screen.blit(ball, (x, y))

        # Wrapping code
        x += dx
        if x >= screen.get_width():
            x = - ball.get_width()
        screen.blit(background, (0, 0))
        screen.blit(ball, (x, y))

                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
