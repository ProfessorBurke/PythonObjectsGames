"""Simple sound program."""

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
    """Create a window and process events related to sound."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Press the space bar")
    screen.fill((140, 211, 226))
    pygame.display.flip()
    clock: pygame.time.Clock = pygame.time.Clock()
    hop: pygame.mixer.Sound

    # Load sound
    if pygame.mixer:
        hop = pygame.mixer.Sound(file = "hop.ogg")

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Process space bar press to play sound.
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_SPACE:
                    if pygame.mixer:
                        hop.play()
    pygame.quit()

main()
