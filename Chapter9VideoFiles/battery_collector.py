"""Add the program description here."""

# Imports and initialize pygame.
import random
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
    battery: pygame.Surface
    robotx: int
    roboty: int
    battery1x: int
    battery1y: int
    battery2x: int
    battery2y: int
    counter: int = 0
    distance1: int
    distance2: int
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    screen = make_window(SIZE, caption)
    background = pygame.Surface((SIZE, SIZE))
    background.fill((255, 255, 255))
    robot = pygame.image.load("robot.jpg").convert()
    battery = pygame.image.load("battery.jpg").convert()
    robotx = random.randint(0, screen.get_width() - robot.get_width())
    roboty = random.randint(0, screen.get_height() - robot.get_height())
    battery1x = random.randint(0, screen.get_width() - battery.get_width())
    battery1y = random.randint(0, screen.get_height() - battery.get_height())
    battery2x = random.randint(0, screen.get_width() - battery.get_width())
    battery2y = random.randint(0, screen.get_height() - battery.get_height())
    clock: pygame.time.Clock = pygame.time.Clock()

    # Process events until the user chooses to quit.
    while not user_quit:
        # Count to two minutes
        counter += 1
        if counter  == 60:
            # Move robot to the closest battery
            distance1 = math.sqrt((robotx - battery1x) ** 2
                                  + (roboty - battery1y) ** 2)
            distance2 = math.sqrt((robotx - battery2x) ** 2
                                  + (roboty - battery2y) ** 2)
            if distance1 < distance2:
                robotx = battery1x
                roboty = battery1y
            else:
                robotx = battery2x
                roboty = battery2y
        elif counter == 120:
            counter = 0
            robotx = random.randint(0, screen.get_width() - robot.get_width())
            roboty = random.randint(0, screen.get_height() - robot.get_height())
            battery1x = random.randint(0, screen.get_width() - battery.get_width())
            battery1y = random.randint(0, screen.get_height() - battery.get_height())
            battery2x = random.randint(0, screen.get_width() - battery.get_width())
            battery2y = random.randint(0, screen.get_height() - battery.get_height())

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
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw the background.
        screen.blit(background, (0, 0))
        screen.blit(robot, (robotx, roboty))
        screen.blit(battery, (battery1x, battery1y))
        screen.blit(battery, (battery2x, battery2y))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
