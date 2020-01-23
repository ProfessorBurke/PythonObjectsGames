"""A simple object demonstration."""

from StarBurst import *
import pygame
pygame.init()

def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen


def main() -> None:
    """Create and draw two StarBursts."""
    # Annotate and initialize variables.
    SIZE: int = 480
    screen: pygame.Surface
    stars: list
    burst1: StarBurst
    burst2: StarBurst
    user_quit: bool
    event: pygame.Event
    
    # Set up assets.
    screen = make_window(SIZE, "Fireworks!")
    stars = [pygame.image.load("small_red_star.png"),
             pygame.image.load("small_blue_star.png"),
             pygame.image.load("small_green_star.png"),
             pygame.image.load("small_yellow_star.png")]


    # Make two starbursts and draw them.
    burst1 = StarBurst(136, 225, random.choice(stars))
    burst2 = StarBurst(312, 128, random.choice(stars))
    burst1.draw_burst(screen)
    burst2.draw_burst(screen)
    pygame.display.flip()
    
    # Wait for the user to close the window.
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
    pygame.quit()

main()
