"""Add the program description here."""

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class WrappingBall(pygame.sprite.Sprite):

    # Annotate object-level fields
    _dx: int

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize a ball instance with image at x,y."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 5

    def update(self, screen: pygame.Surface) -> None:
        self.rect.centerx += self._dx
        if self.rect.left >= screen.get_width():
            self.rect.right = 0
        

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Add a function description."""
    # Annotate and initialize variables
    WIDTH: int = 640
    HEIGHT: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    wrapping_ball: WrappingBall
    ball_group: pygame.sprite.Group = pygame.sprite.Group()
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"
    x: int = 0
    y: int = 200
    dx: int = 5
    i: int

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    ball_image: pygame.Surface = pygame.image.load("ball.gif").convert()
    for i in range(8):
        wrapping_ball = WrappingBall(ball_image,
                                     random.randint(0, WIDTH),
                                     random.randint(0, HEIGHT))
        ball_group.add(wrapping_ball)

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
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass

                
        # Update and draw.
        ball_group.clear(screen, background)
        ball_group.update(screen)
        ball_group.draw(screen)
        pygame.display.flip()
    pygame.quit()

main()
