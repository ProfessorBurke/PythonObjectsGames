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
    dark_rooms: pygame.Surface
    light_rooms: pygame.Surface
    blit_rooms: pygame.Surface
    dark_raccoon: pygame.Surface
    light_raccoon: pygame.Surface
    blit_raccoon: pygame.Surface
    window_upper_left: pygame.Rect
    window_upper_right: pygame.Rect
    window_lower_left: pygame.Rect
    window_lower_right: pygame.Rect
    windows: list
    outside: pygame.Surface
    user_quit: bool = False
    raccoon_x: int
    raccoon_y: int
    light_index: int
    e: pygame.event.Event
    caption: str = "Turn on the lights in a room by clicking"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    dark_rooms = pygame.image.load("dark_rooms_background.jpg").convert()
    light_rooms = pygame.image.load("light_rooms_background.jpg").convert()
    dark_raccoon = pygame.image.load("dark_raccoon.png").convert_alpha()
    light_raccoon = pygame.image.load("raccoon.png").convert_alpha()
    outside = pygame.image.load("outside.jpg").convert()
    window_upper_left = pygame.Rect(88, 36, 184, 160)
    window_upper_right = pygame.Rect(411, 36, 188, 164)
    window_lower_left = pygame.Rect(84, 298, 187, 161)
    window_lower_right = pygame.Rect(408, 297, 191, 164)
    windows = [window_upper_left, window_upper_right, window_lower_left,
               window_lower_right]
    light_index = -1
    blit_rooms = dark_rooms
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
                for i in range(len(windows)):
                    if windows[i].collidepoint(e.__dict__["pos"]):
                        light_index = i
                raccoon_x = random.randint(0, screen.get_width() - blit_raccoon.get_width())
                raccoon_y = random.randint(0, screen.get_height() - blit_raccoon.get_height())
                if windows[light_index].colliderect((raccoon_x,
                                                     raccoon_y,
                                                     blit_raccoon.get_width(),
                                                     blit_raccoon.get_height())):
                    blit_raccoon = pygame.transform.flip(light_raccoon,
                                                         False, True)
                else:
                    blit_raccoon = dark_raccoon
                                                                        
        # Draw the room and raccoon.
        screen.blit(outside, (0, 0))
        for i in range(len(windows)):
            screen.set_clip(windows[i])
            if i == light_index:
                screen.blit(light_rooms, (0, 0))
            else:
                screen.blit(dark_rooms, (0, 0))
            screen.blit(blit_raccoon, (raccoon_x, raccoon_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
