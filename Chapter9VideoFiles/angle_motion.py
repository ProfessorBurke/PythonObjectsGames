"""Add the program description here."""

# Imports and initialize pygame.
import math
import pygame
pygame.init()

def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Add a function description."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    robot: pygame.Surface
    robot_x: float = SIZE / 2
    robot_y: float = SIZE / 2
    angle: float = 36.87
    speed: int = 5
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.Surface((SIZE, SIZE))
    background.fill((255, 255, 255))
    robot = pygame.image.load("robot.jpg")
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEMOTION:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif e.type == pygame.MOUSEBUTTONUP:
                robot_x += speed * math.cos(math.radians(angle))
                robot_y += speed * math.sin(math.radians(-angle))
            elif e.type == pygame.KEYDOWN:
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw the background.
        screen.blit(background, (0, 0))
        screen.blit(robot, (robot_x, robot_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
