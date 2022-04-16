"""Motion that includes drag."""

# Constants for drawing
LEFT = 0
TOP = 3
RIGHT = 2
BOTTOM = 1
NO_JETS = -1

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

def draw_jets(direction: int, surf: pygame.Surface, bubbles: pygame.Surface) -> None:
    """Draw the jets along the edge of the Surface."""
    blit_bubbles: pygame.Surface = pygame.transform.rotate(bubbles, direction * 90)       
    if direction == LEFT:
        for i in range(20, surf.get_height() - bubbles.get_height(), 50):
            surf.blit(blit_bubbles, (0, i))
    elif direction == RIGHT:
        for i in range(20, surf.get_height() - bubbles.get_height(), 50):
            surf.blit(blit_bubbles, (surf.get_width() - blit_bubbles.get_width(), i))
    elif direction == TOP:
        for i in range(20, surf.get_width() - bubbles.get_width(), 50):
            surf.blit(blit_bubbles, (i, 0))
    elif direction == BOTTOM:
        for i in range(20, surf.get_width() - bubbles.get_width(), 50):
            surf.blit(blit_bubbles, (i, surf.get_height() - blit_bubbles.get_height()))

def main() -> None:
    """Draw an image centered and at the boundaries."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    CHANGE = 10
    screen: pygame.Surface
    background: pygame.Surface
    pineapple: pygame.Surface
    bubbles: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    drag: float = .96 
    x: float = SCREEN_SIZE / 2
    y: float = SCREEN_SIZE / 2
    dx: float = 0
    dy: float = 0
    jets: int = NO_JETS
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Press arrow keys for jets")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((140, 211, 226))
    pineapple = pygame.image.load("small_pineapple.png")
    pineapple.convert_alpha()
    bubbles = pygame.image.load("bubbles.png")
    bubbles.convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_UP:
                    dy += -CHANGE
                    jets = BOTTOM
                elif e.__dict__["key"] == pygame.K_DOWN:
                    dy += CHANGE
                    jets = TOP
                elif e.__dict__["key"] == pygame.K_LEFT:
                    dx += -CHANGE
                    jets = RIGHT
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    dx += CHANGE
                    jets = LEFT
            elif e.type == pygame.KEYUP:
                jets = -1

        # Move the pineapple.
        dx *= drag
        dy *= drag
        x += dx
        y += dy

        # Check boundaries
        if x < 0:
            x = 0
            dx *= -1
        elif x + pineapple.get_width() > screen.get_width():
            x = screen.get_width() - pineapple.get_width()
            dx *= -1
        if y < 0:
            y = 0
            dy *= -1
        elif y + pineapple.get_height() > screen.get_height():
            y = screen.get_height() - pineapple.get_height()
            dy *= -1
                 
        # Draw to the screen and show.
        screen.blit(background, (0, 0))
        draw_jets(jets, screen, bubbles)
        screen.blit(pineapple, (x, y))
        pygame.display.flip()
         
    pygame.quit()

main()
