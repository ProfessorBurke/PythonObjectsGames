"""Illustrate transformations."""

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
    """Process keypresses to transform an image."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    rotation: int = 0
    screen: pygame.Surface
    background: pygame.Surface
    pineapple: pygame.Surface
    blit_pineapple: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Transformation Demo")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((140, 211, 226))
    pineapple = pygame.image.load("cool_pineapple.png")
    pineapple= pineapple.convert_alpha()
    blit_pineapple = pineapple
    clock: pygame.time.Clock = pygame.time.Clock()
    
    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            if e.type == pygame.KEYDOWN:
                # Flip, scale, or rotate based on key press.
                if e.__dict__["key"] == pygame.K_RIGHT:
                    blit_pineapple = pygame.transform.flip(pineapple, True, False)
                elif e.__dict__["key"] == pygame.K_UP:
                    blit_pineapple = pygame.transform.flip(pineapple, False, True)
                elif e.__dict__["key"] == pygame.K_SPACE:
                    rotation += 30
                    blit_pineapple = pygame.transform.rotate(pineapple, rotation)
                elif e.__dict__["key"] == pygame.K_m:
                    blit_pineapple = pygame.transform.scale(pineapple,
                                                            (int(pineapple.get_width() * 1.5),
                                                             int(pineapple.get_height() * 1.5)))
                # These keys undo flipping and scaling:
                elif (e.__dict__["key"] == pygame.K_s
                      or e.__dict__["key"] == pygame.K_LEFT
                      or e.__dict__["key"] == pygame.K_DOWN):
                    blit_pineapple = pineapple
                
        # Calculate pineapple coordinates for the middle of the screen.
        center_xcoord: float = (background.get_width() / 2) - (blit_pineapple.get_width() / 2)
        center_ycoord: float = (background.get_height() / 2) - (blit_pineapple.get_height() / 2)
        # Draw to the screen and show.
        screen.blit(background, (0, 0))
        screen.blit(blit_pineapple, (center_xcoord, center_ycoord))
        pygame.display.flip()
         
    pygame.quit()

main()
