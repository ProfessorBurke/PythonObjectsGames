"""Demonstrate a falling equation."""

# Import and initialize pygame.
import pygame
pygame.init()

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Move an image randomly on the screen."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    pisa_x: int = 0
    pisa_y: int = 0
    pisa: pygame.Surface
    small_ball_x: float = 138
    large_ball_x: float = 208
    y_start: float = 24
    small_ball_y: float = y_start
    large_ball_y : float = y_start
    large_ball: pygame.Surface
    small_ball: pygame.Surface
    time: float = 0
    drop: bool = False
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Pisa Gravity Experiment")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    large_ball = pygame.image.load("large_ball.png")
    large_ball = large_ball.convert_alpha()
    small_ball = pygame.image.load("small_ball.png")
    small_ball = small_ball.convert_alpha()
    pisa = pygame.image.load("pisa.png")
    pisa = pisa.convert_alpha()
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Process space bar as jump and arrow key as move.
            elif e.type == pygame.KEYDOWN:
                 if e.__dict__["key"] == pygame.K_SPACE:
                    drop = True
                    
        # Calculate new y coordinates for balls
        if drop:
            time += 1 / 30
            small_ball_y = y_start + .5 * 78 * time ** 2
            large_ball_y = small_ball_y
            # Check if we've hit the ground
            if large_ball_y + large_ball.get_height() >= screen.get_height():
                small_ball_y = screen.get_height() - small_ball.get_height()
                large_ball_y = screen.get_height() - large_ball.get_height()
                drop = False
        
        # Draw to the screen and show.
        screen.blit(background, (0, 0))
        screen.blit(pisa, (pisa_x, pisa_y))
        screen.blit(large_ball, (large_ball_x, large_ball_y))
        screen.blit(small_ball, (small_ball_x, small_ball_y))
        pygame.display.flip()
         
    pygame.quit()

main()
