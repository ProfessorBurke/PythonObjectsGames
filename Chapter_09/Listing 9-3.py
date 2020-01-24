"""Allow the user to change the direction of the arrow
   without changing the speed."""

# Imports and initialize pygame.
import math
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
    blit_image: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    x: float = 0
    y: float = 0
    speed: int = 3
    angle: float = 0
    dx: float
    dy: float
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Changing vector direction")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    image = pygame.image.load("arrow.png")
    image = image.convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_RIGHT:
                    angle += 10
                elif e.__dict__["key"] == pygame.K_LEFT:
                    angle -= 10
 
        # Calculate dx and dy according to angle and speed.
        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))
        x += dx
        y += dy
                 
        # Draw to the screen and show.
        blit_image = pygame.transform.rotate(image, -angle)
        screen.blit(background, (0, 0))
        screen.blit(blit_image, (x, y))
        pygame.display.flip()
         
    pygame.quit()

main()
