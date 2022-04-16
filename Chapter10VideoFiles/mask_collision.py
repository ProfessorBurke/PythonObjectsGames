"""Collision detection."""

# Imports and initialize pygame.
import random
import math
import pygame
pygame.init()


class Pineapple(pygame.sprite.Sprite):
    """A player-controlled pineapple."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize pineapple with a mask."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("small_pineapple.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.top = random.randint(0, screen.get_height()
                                       - self.rect.bottom)
        self.rect.left = random.randint(0, screen.get_width()
                                        - self.rect.right)

    def move_left(self) -> None:
        """Move five pixels left."""
        self.rect.left -= 5

    def move_right(self) -> None:
        """Move five pixels right."""
        self.rect.left += 5

    def move_up(self) -> None:
        """Move five pixels up."""
        self.rect.top -= 5

    def move_down(self) -> None:
        """Move five pixels down."""
        self.rect.top += 5

class SpikeyFloat(pygame.sprite.Sprite):
    """A non-moving circle."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize a spikey toy with a mask."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spikey_toy.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = random.randint(0, screen.get_width() / 4)
        self.rect.top = random.randint(0, screen.get_height() / 4)

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Detect collisions between car and hazards."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    pineapple: Pineapple
    pineapple_group: pygame.sprite.Group
    toy: SpikeyFloat
    toy_group: pygame.sprite.Group
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Arrow keys move the pineapple")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    # Make circles and groups
    pineapple = Pineapple(screen)
    pineapple_group = pygame.sprite.Group(pineapple)        
    toy = SpikeyFloat(screen)
    toy_group = pygame.sprite.Group(toy)
    crashed = False

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    pineapple.move_left()
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    pineapple.move_right()
                elif e.__dict__["key"] == pygame.K_UP:
                    pineapple.move_up()
                elif e.__dict__["key"] == pygame.K_DOWN:
                    pineapple.move_down()
                
 
        # Check for collisions
        collided_toys = pygame.sprite.spritecollide(pineapple,
                                                    toy_group, False,
                                                    pygame.sprite.collide_mask)
        for toy in collided_toys:
            print("CRASH!")
                
        # Draw to the screen and show.
        toy_group.clear(screen, background)
        pineapple_group.clear(screen, background)
        pineapple_group.update(screen)
        toy_group.draw(screen)
        pineapple_group.draw(screen)

        pygame.display.flip()
         
    pygame.quit()

main()
