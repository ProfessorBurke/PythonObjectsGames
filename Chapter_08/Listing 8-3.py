"""Move with the keyboard."""

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
    """Process keyboard events by reacting with a blob."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    blob: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    blob_x: int = 0
    blob_y: int = 0
    speed_mult: int = 1

    # Set up assets.
    screen = make_window(SIZE, "The blob!")
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
            # Move the blob.
            elif e.type == pygame.KEYDOWN:
                # Control key for double speed.
                if e.__dict__["mod"] & pygame.KMOD_CTRL:
                    speed_mult = 2
                else:
                    speed_mult = 1
                # Arrow keys for direction.
                if e.__dict__["key"] == pygame.K_UP:
                    blob_y -= 3 * speed_mult
                elif e.__dict__["key"] == pygame.K_DOWN:
                    blob_y += 3 * speed_mult
                elif e.__dict__["key"] == pygame.K_LEFT:
                    blob_x -= 3 * speed_mult
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    blob_x += 3 * speed_mult
                # Space bar to draw the blob permanently.
                elif e.__dict__["key"] == pygame.K_SPACE:
                    background.blit(blob, (blob_x, blob_y))
                    
        # Draw the background and blob.
        screen.blit(background, (0, 0))
        screen.blit(blob, (blob_x, blob_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
