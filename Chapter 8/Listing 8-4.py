"""Illustrate transparency options."""

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
    """Draw images with different transparency settings."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    star: pygame.Surface
    alpha_star: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event

    # Set up assets.
    screen = make_window(SIZE, "Transparency Demo")
    background = pygame.image.load("checkerboard.jpg")
    star = pygame.image.load("star.gif")
    star = star.convert()
    alpha_star = pygame.image.load("alpha_star.png")
    alpha_star = alpha_star.convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Draw the background and stars.
    screen.blit(background, (0, 0))
    # Star with no transparency.
    screen.blit(star, (50, 100))
    ##print(star.get_alpha()) #None
    # Star with transparent background.
    star.set_colorkey((255, 255, 255))
    screen.blit(star, (200, 100))
    # Star with less opacity.
    star.set_alpha(150)
    star.set_colorkey(None)
    screen.blit(star, (350, 100))
    ##print(star.get_alpha()) #150
    # Star with an alpha channel.
    screen.blit(alpha_star, (200, 250))

    # Show the display.
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
