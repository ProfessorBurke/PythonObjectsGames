"""Demonstrate unit vectors with variable speed."""

# Imports and initialize pygame.
import math
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
    """Move an image randomly on the screen and chase it."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    ball: pygame.Surface
    target: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    ball_x: float = 0
    ball_y: float = 0
    target_x: int = 0
    target_y: int = 0
    base_speed: int = 2
    speed: float
    unit_dx: float
    unit_dy: float
    count: int = 0
    distance_x: float
    distance_y: float
    distance: float
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Unit vector demonstration")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    ball = pygame.image.load("ball.png")
    ball = ball.convert_alpha()
    target = pygame.image.load("target.png")
    target = target.convert_alpha()
    target_x = random.randint(0, screen.get_width() - target.get_width())
    target_y = random.randint(0, screen.get_height() - target.get_height())
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True

        # Randomly generate a location for the target periodically.
        if count == 45:
            count = 0
            target_x = random.randint(0, screen.get_width() - target.get_width())
            target_y = random.randint(0, screen.get_height() - target.get_height())
        count += 1

        # Determine the unit offsets for the ball.
        distance_x = (target_x + target.get_width()/2) - (ball_x + ball.get_width()/2)
        distance_y = (target_y + target.get_height()/2) - (ball_y + ball.get_height()/2)
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        unit_dx = distance_x / distance
        unit_dy = distance_y / distance

        # Decrease the speed as the ball gets closer to target.
        speed = base_speed * (distance / (screen.get_width() / 5))
        
        # Multiply offsets by speed and move ball.
        ball_x += speed * unit_dx
        ball_y += speed * unit_dy
                 
        # Draw to the screen and show.
        screen.blit(background, (0, 0))
        screen.blit(target, (target_x, target_y))
        screen.blit(ball, (ball_x, ball_y))
        pygame.display.flip()
         
    pygame.quit()

main()
