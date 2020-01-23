"""Basic motion with boundary checking."""

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
    """Move an image randomly on the screen."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    image: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    x: int = 0
    y: int = 0
    dx: int = 5
    dy: int = 5
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Basic Motion")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    image = pygame.image.load("ball.gif")
    image = image.convert()
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
 
        # Change x and y.
        x += dx
        y += dy
        
        # Check boundaries and adjust.
        if x < 0:
            x = 0
            dx *= -1
        elif x + image.get_width() > screen.get_width():
            x = screen.get_width() - image.get_width()
            dx *= -1
        if y < 0:
            y = 0
            dy *= -1
        elif y + image.get_height() > screen.get_height():
            y = screen.get_height() - image.get_height()
            dy *= -1
                 
        # Draw to the screen and show.
        screen.blit(background, (0, 0))
        screen.blit(image, (x, y))
        pygame.display.flip()
         
    pygame.quit()

main()
