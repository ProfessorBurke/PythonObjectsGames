"""Collision detection."""

# Imports and initialize pygame.
import random
import math
import pygame
pygame.init()


class MovingCircle(pygame.sprite.Sprite):
    """A player-controlled circle."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize a circle with a radius."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80,80))
        self.image.fill((255, 255, 0))
        pygame.draw.circle(self.image, (0, 0, 200), (40,40), 40)
        self.rect = self.image.get_rect()
        self.radius = 40
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

class Circle(pygame.sprite.Sprite):
    """A non-moving circle."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize a circle with a radius."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill((0, 255, 0))
        pygame.draw.circle(self.image, (255,0,0), (40,40), 40)
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.left = random.randint(0, screen.get_width() / 3)
        self.rect.top = random.randint(0, screen.get_height() / 3)

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
    moving_circle: MovingCircle
    moving_group: pygame.sprite.Group
    circle: Circle
    sitting_group: pygame.sprite.Group
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Arrow keys move the blue circle")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((225, 225, 225))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    # Make circles and groups
    circle = Circle(screen)
    sitting_group = pygame.sprite.Group(circle)        
    moving_circle = MovingCircle(screen)
    moving_group = pygame.sprite.Group(moving_circle)
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
                    moving_circle.move_left()
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    moving_circle.move_right()
                elif e.__dict__["key"] == pygame.K_UP:
                    moving_circle.move_up()
                elif e.__dict__["key"] == pygame.K_DOWN:
                    moving_circle.move_down()
                
 
        # Check for collisions
        # Using collide_rect (default)
##        collided_circles = pygame.sprite.spritecollide(moving_circle,
##                                                    sitting_group, False)
        # using collide_circle
        collided_circles = pygame.sprite.spritecollide(moving_circle,
                                                    sitting_group, False,
                                                    pygame.sprite.collide_circle)
        for circle in collided_circles:
            print("CRASH!")
            
                
        # Draw to the screen and show.
        sitting_group.clear(screen, background)
        sitting_group.draw(screen)

        moving_group.clear(screen, background)
        moving_group.update(screen)
        moving_group.draw(screen)

        pygame.display.flip()
         
    pygame.quit()

main()
