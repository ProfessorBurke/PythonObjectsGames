"""Illustrate the draw module."""

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
    """Demonstrate the draw module functions."""
    # Annotate and initialize variables
    WIDTH: int = 480
    HEIGHT: int = 480
    screen: pygame.Surface
    bg: pygame.Surface 
    user_quit: bool = False
    e: pygame.event.Event

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, "Draw Demo")
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((255, 255, 255))
    clock: pygame.time.Clock = pygame.time.Clock()

    # Demonstrate one of each draw command.
    poly_points: list = [(60, 30), (20, 110), (60, 190), (100, 110)]
    line_points: list = [(400, 30), (350, 60), (400, 90), (450, 60)]
    aa_line_points: list = [(410, 40), (360, 70), (410, 100), (460, 70)]
    pygame.draw.rect(bg, (255, 0, 0), (10, 10, 100, 200), 5)
    pygame.draw.polygon(bg, (0, 255, 0), poly_points, 3)
    pygame.draw.circle(bg, (0, 0, 255), (240, 240), 50, 10)
    pygame.draw.ellipse(bg, (255, 255, 0), (10, 10, 100, 200), 10)
    pygame.draw.arc(bg, (0, 255, 255), (300, 250, 100, 200), 0, math.pi / 2, 5)
    pygame.draw.line(bg, (255, 0, 255), (0, 420), (200, 300), 1)
    pygame.draw.aaline(bg, (255, 0, 255), (0, 430), (200, 310), True)
    pygame.draw.lines(bg, (0, 0, 0), False, line_points, 1)
    pygame.draw.aalines(bg, (0, 0, 0), False, aa_line_points, True)
    
    # Draw to the screen and show.
    screen.blit(bg, (0, 0))
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
