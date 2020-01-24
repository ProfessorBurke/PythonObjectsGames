"""Layered groups."""

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class Firefly(pygame.sprite.Sprite):
    """A firefly sprite."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = pygame.Surface((4,4))
        pygame.draw.circle(self.image, (255, 255, 255),(2, 2), 2)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(0, screen.get_height() - self.rect.height)
        self.rect.left = random.randint(0, screen.get_width() - self.rect.width)

class Camper(pygame.sprite.Sprite):
    """A moving camper silhouette"""

    # Annotate object-level fields
    _dx: int

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = pygame.image.load("camper.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = screen.get_height() - self.rect.height
        self.rect.left = random.randint(0, screen.get_width() - self.rect.width)
        self._dx = random.randint(1, 3)

    def update(self, screen: pygame.Surface) -> None:
        """Move left to right and back."""
        self.rect.centerx += self._dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self._dx *= -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self._dx *= -1

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
    campers: pygame.sprite.Group
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
    campers = pygame.sprite.Group(camper)

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                
        # Draw to the screen and show.
        fireflies.clear(screen, background)
        campers.clear(screen, background)
        fireflies.update()
        campers.update(screen)
        fireflies.draw(screen)
        campers.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
