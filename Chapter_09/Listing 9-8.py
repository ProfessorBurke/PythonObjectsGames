"""Scrolling background demo."""

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
    """The arrow keys move the penguin or scroll."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    LEFT: int = 0
    RIGHT: int = 1
    NOT_MOVING: int = -1
    screen: pygame.Surface
    background: pygame.Surface
    penguin_left: pygame.Surface
    penguin_right: pygame.Surface
    penguin: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    penguin_x: int = 0
    penguin_y: int = SCREEN_SIZE - 138
    background_x: int = 0
    background_y: int = 0
    move_amount: int = 5
    scroll_threshold: int = 100
    moving: int = NOT_MOVING
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Scrolling Background")
    background = pygame.image.load("icecastle.jpg")
    background = background.convert()
    penguin_right = pygame.image.load("penguin.png")
    penguin_right = penguin_right.convert_alpha()
    penguin_left = pygame.transform.flip(penguin_right, True, False)
    penguin = penguin_right
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    moving = LEFT
                    penguin = penguin_left
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    moving = RIGHT
                    penguin = penguin_right
            elif e.type == pygame.KEYUP:
                moving = NOT_MOVING
 
        # Move the penguin or the background
        if moving == LEFT:
            if penguin_x < scroll_threshold and background_x < 0:
                background_x += move_amount
                if background_x > 0:
                    background_x = 0
            else:
                penguin_x -= move_amount
                if penguin_x < 0:
                    penguin_x = 0
        elif moving == RIGHT:
            if (penguin_x + penguin.get_width() > screen.get_width() - scroll_threshold
                   and background_x + background.get_width() > screen.get_width()):
                background_x -= move_amount
                if background_x + background.get_width() < screen.get_width():
                    background_x = -(background.get_width()-screen.get_width())
            else:
                penguin_x += move_amount
                if penguin_x > screen.get_width() - penguin.get_width():
                    penguin_x = screen.get_width() - penguin.get_width()

        # Draw to the screen and show.
        screen.blit(background, (background_x, background_y))
        screen.blit(penguin, (penguin_x, penguin_y))
        pygame.display.flip()
         
    pygame.quit()

main()
