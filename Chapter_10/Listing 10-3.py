"""Generating multiple sprites."""

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class Ball(pygame.sprite.Sprite):
    """A bouncing ball sprite."""

    # Annotate object-level fields
    _dx: float
    _dy: float

    def __init__(self, image: pygame.Surface, x: float, y: float,
                 dx: float, dy: float) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = dx
        self._dy = dy

    def update(self, screen: pygame.Surface) -> None:
        """Move the ball and check boundaries."""
        self.rect.centerx += self._dx
        self.rect.centery += self._dy
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self._dx *= -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self._dx *= -1
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
            self._dy *= -1
        elif self.rect.top < 0:
            self.rect.top = 0
            self._dy *= -1

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
    ball: Ball
    sprites: pygame.sprite.Group
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Basic Motion")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    screen.blit(background, (0, 0))
    sprites = pygame.sprite.Group()        
    for i in range(10):
        ball = Ball(pygame.image.load("ball.gif").convert(),
                    random.randint(0, 200),random.randint(0, 200),
                    random.randint(1, 7),random.randint(1, 7))
        sprites.add(ball)
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                
        # Draw to the screen and show.
        sprites.clear(screen, background)
        sprites.update(screen)
        sprites.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
