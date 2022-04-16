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
    LEFT: int = 0
    RIGHT: int = 1
    NOT_MOVING: int = -1
    screen: pygame.Surface
    background: pygame.Surface
    robot: pygame.Surface
    bkgd_x: int = 0
    bkgd_y: int = 0
    dx: int = 5
    robot_x: int = 0
    robot_y: int
    scroll_threshold: int = 100
    moving: int = NOT_MOVING
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.image.load("cityscape.jpg")
    robot = pygame.image.load("rocket_robot.png")
    robot_y = screen.get_height() - robot.get_height()
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
                pass
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    moving = LEFT
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    moving = RIGHT
            elif e.type == pygame.KEYUP:
                moving= NOT_MOVING
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Move and draw the robot or the background.
        robot_right: int = robot_x + robot.get_width()
        bkgd_right: int = bkgd_x + background.get_width()
        if moving == RIGHT:
            if (robot_right > screen.get_width()- scroll_threshold
                and bkgd_right > screen.get_width()):
                bkgd_x -= dx
                if bkgd_x + background.get_width() < screen.get_width():
                    bkgd_x = screen.get_width() - background.get_width()
            else:
                robot_x += dx
                if robot_x + robot.get_width() > screen.get_width():
                    robot_x = screen.get_width() - robot.get_width()
        elif moving == LEFT:
            if robot_x < scroll_threshold and bkgd_x < 0:   
                bkgd_x += dx
                if bkgd_x > 0:
                    bkgd_x = 0
            else:
                robot_x -= dx
                if robot_x < 0:
                    robot_x = 0
        screen.blit(background, (bkgd_x, bkgd_y))
        screen.blit(robot, (robot_x, robot_y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
