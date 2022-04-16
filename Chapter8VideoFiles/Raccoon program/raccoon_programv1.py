"""Turn on the lights to move the raccoon from the room."""

# Import libraries and initialize pygame.
import random
import pygame
pygame.init()

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Process clicks by turning on lights and moving the raccoon."""
    # Annotate and initialize variables
    WIDTH: int = 640
    HEIGHT: int = 480
    screen: pygame.Surface
    dark_room: pygame.Surface
    light_room: pygame.Surface
    blit_room: pygame.Surface
    dark_raccoon: pygame.Surface
    light_raccoon: pygame.Surface
    blit_raccoon: pygame.Surface
    user_quit: bool = False
    dark: bool = True
    raccoon_x: int
    raccoon_y: int
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    dark_room = pygame.image.load("parlor_dark_full_window.jpg").convert()
    light_room = pygame.image.load("parlor_full_window.jpg").convert()
    dark_raccoon = pygame.image.load("dark_raccoon.png").convert_alpha()
    light_raccoon = pygame.image.load("raccoon.png").convert_alpha()
    blit_room = dark_room
    blit_raccoon= dark_raccoon
    clock: pygame.time.Clock = pygame.time.Clock()

    raccoon_x = random.randint(0, screen.get_width() - blit_raccoon.get_width())
    raccoon_y = random.randint(0, screen.get_height() - blit_raccoon.get_height())

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEBUTTONUP:
                if dark:
                    # Toggle from dark to light
                    blit_raccoon = light_raccoon
                    blit_room = light_room
                    dark = False
                    raccoon_x = random.randint(0, screen.get_width() - blit_raccoon.get_width())
                    raccoon_y = random.randint(0, screen.get_height() - blit_raccoon.get_height())
                else:
                    # Toggle from light to dark
                    blit_raccoon = dark_raccoon
                    blit_room = dark_room
                    dark = True
                    
        # Draw the room and raccoon.
        screen.blit(blit_room, (0, 0))
        screen.blit(blit_raccoon, (raccoon_x, raccoon_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
