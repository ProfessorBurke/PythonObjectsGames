"""Add the program description here."""

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
    """Add a function description."""
    # Annotate and initialize variables
    SIZE: int = 480
    GRAVITY: int = 745
    screen: pygame.Surface
    background: pygame.Surface
    robot: pygame.Surface
    robot_x: int = 200
    robot_y: int = 0
    robot_initial_y: int = 0
    time: float = 0
    user_quit: bool = False
    falling: bool = False
    e: pygame.event.Event
    caption: str = "Click to drop the robot"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.image.load("city.jpg").convert()
    robot = pygame.image.load("robot.png").convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        if falling:
            time += 1/30
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEMOTION:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif e.type == pygame.MOUSEBUTTONUP:
                falling = True
            elif e.type == pygame.KEYDOWN:
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw the background.
        if falling:
            robot_y = robot_initial_y + .5 * GRAVITY * time ** 2
        screen.blit(background, (0, 0))
        screen.blit(robot, (robot_x, robot_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
