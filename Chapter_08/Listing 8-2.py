"""Move with the mouse."""

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
    """Process mouse events by reacting with a blob."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    blob: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    blob_x: int = 0
    blob_y: int = 0
    caption: str = "The blob!"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.Surface((SIZE, SIZE))
    background.fill((255, 255, 255))
    blob = pygame.image.load("blob.png")
    blob = blob.convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Change the caption.
            elif e.type == pygame.ACTIVEEVENT:
                if e.__dict__["gain"] == 0:
                    pygame.display.set_caption("Come back!")
                else:
                    pygame.display.set_caption(caption)
            # Move the blob.
            elif e.type == pygame.MOUSEMOTION:
                blob_x = e.__dict__["pos"][0]
                blob_y = e.__dict__["pos"][1]
            # Draw the blob to the screen permanently.
            elif e.type == pygame.MOUSEBUTTONDOWN:
                background.blit(blob, (e.__dict__["pos"][0],
                                       e.__dict__["pos"][1]))
                    
        # Draw the background and blob.
        screen.blit(background, (0, 0))
        screen.blit(blob, (blob_x, blob_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
