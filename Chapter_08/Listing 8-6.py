"""Illustrate clipping regions."""

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
    """Draw images within clipping regions."""
    # Annotate and initialize variables
    WIDTH: int = 480
    HEIGHT: int = 300
    screen: pygame.Surface
    background: pygame.Surface
    photo1: pygame.Surface
    photo2: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, "Clipping Demo")
    background = pygame.image.load("frames_background.jpg")
    photo1 = pygame.image.load("photo1.jpg")
    photo1 = photo1.convert()
    photo2 = pygame.image.load("photo2.jpg")
    photo2 = photo2.convert()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Set the clipping region and draw the first photo.
    background.set_clip(52, 59, 114, 183)
    background.blit(photo1, (50, 50))
    # Set the clipping region and draw the second photo.
    background.set_clip(315, 59, 114, 183)
    background.blit(photo2, (315, 59))
    # Draw to the screen and show.
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
