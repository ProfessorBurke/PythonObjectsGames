"""Sprite variations."""

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class Firefly(pygame.sprite.Sprite):
    """A firefly sprite."""

    # Annotate object-level fields
    _max_time: int
    _timer: int

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = pygame.Surface((4,4))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(0, screen.get_height() - self.rect.height)
        self.rect.left = random.randint(0, screen.get_width() - self.rect.width)
        self._max_time = random.randint(500, 1000)
        self._timer = random.randint(1, self._max_time)

    def update(self) -> None:
        """Increment the timer and flash when it goes off."""
        self._timer += 1
        if self._timer == self._max_time:
            pygame.draw.circle(self.image, (255, 255, 255),(2, 2), 2)
            self._timer = 0
        elif self._timer == 10:
            self.image.fill((0, 0, 0))

class Camper(pygame.sprite.Sprite):
    """A moving camper sillhouette"""

    # Annotate object-level fields
    _speed: int
    _dx: int

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = pygame.image.load("camper.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = screen.get_height() - self.rect.bottom
        self.rect.left = random.randint(0, screen.get_width() - self.rect.right)
        self._speed = random.randint(1, 3)
        self._dx = 0

    def update(self, screen: pygame.Surface) -> None:
        """Move the object by _dx and boundary check."""
        self.rect.centerx += self._dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        elif self.rect.left < 0:
            self.rect.left = 0

    def moving(self, multiplier: int) -> None:
        """Set moving state; multiplier is 0 (stop), -1 (left), 1 (right)."""
        self._dx = self._speed * multiplier


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
    firefly: Firefly
    fireflies: pygame.sprite.Group
    camper: Camper
    camper_group: pygame.sprite.Group
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Camping")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    # Make fireflies and group
    fireflies = pygame.sprite.Group()        
    for i in range(20):
        firefly = Firefly(screen)
        fireflies.add(firefly)
    # Make camper and group
    camper = Camper(screen)
    camper_group = pygame.sprite.Group(camper)

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    camper.moving(-1)
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    camper.moving(1)
            elif e.type == pygame.KEYUP:
                camper.moving(0)
                
        # Draw to the screen and show.
        fireflies.clear(screen, background)
        camper_group.clear(screen, background)
        fireflies.update()
        camper_group.update(screen)
        fireflies.draw(screen)
        camper_group.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
