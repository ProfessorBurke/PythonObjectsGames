"""Collision detection."""

# Imports and initialize pygame.
import random
import math
import pygame
pygame.init()


class Car(pygame.sprite.Sprite):
    """A player-controlled car."""

    # Annotate object-level fields
    _speed: int
    _angle: int
    _moving: bool
    _x: float
    _y: float
    _raw_image: pygame.Surface

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self._raw_image = pygame.image.load("tiny_car.png")
        self._raw_image = self._raw_image.convert_alpha()
        self.image = self._raw_image
        self.rect = self.image.get_rect()
        self._x = random.randint(0, screen.get_height()
                                       - self.rect.height)
        self._y = random.randint(0, screen.get_width()
                                        - self.rect.width)
        self.rect.topleft = (self._x, self._y)
        self._speed = 3
        self._angle = 0
        self._moving = False

    def update(self, screen: pygame.Surface) -> None:
        """Move the car (no boundary checking)."""
        if self._moving:
            # Calculate velocity
            dx: float = math.cos(math.radians(self._angle)) * self._speed 
            dy: float = math.sin(math.radians(self._angle)) * self._speed
            # Rotate image and adjust rectangle
            self.image = pygame.transform.rotate(self._raw_image, -self._angle)
            self.rect = self.image.get_rect()
            # Add velocity to (x, y) and set rectangle
            self._x += dx
            self._y += dy
            self.rect.topleft = (self._x, self._y)

    def change_angle(self, increase: bool) -> None:
        """Increase or decrease the angle of motion."""
        if increase:
            self._angle += 10
            if self._angle == 360:
                self._angle = 0
        else:
            self._angle -= 10
            if self._angle == -10:
                self._angle = 350

    def stop_or_go(self) -> None:
        """Start or stop."""
        self._moving = not self._moving

    def slow(self) -> None:
        """Slow the car."""
        if self._speed > 0:
            self._speed -= 1

class Hazard(pygame.sprite.Sprite):
    """A road hazard."""

    def __init__(self, screen: pygame.Surface, image: str) -> None:
        """Initialize from parameters."""
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, screen.get_width()
                                        - self.rect.width)
        self.rect.top = random.randint(0, screen.get_height()
                                       - self.rect.height)

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
    car: Car
    car_group: pygame.sprite.Group
    hazard: Hazard
    hazards: pygame.sprite.Group
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Left and right arrows change direction")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((100, 100, 100))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    # Make hazards and group
    hazards = pygame.sprite.Group()        
    for i in range(10):
        hazard = Hazard(screen, "tiny_cone.png")
        hazards.add(hazard)
    # Make car and group
    car = Car(screen)
    car_group = pygame.sprite.Group(car)

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    car.change_angle(False)
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    car.change_angle(True)
                elif e.__dict__["key"] == pygame.K_SPACE:
                    car.stop_or_go()
 
        # Check for collisions
        crashed_hazards = pygame.sprite.spritecollide(car,
                                                     hazards, True)
        for hazard in crashed_hazards:
            car.slow()
                
        # Draw to the screen and show.
        hazards.clear(screen, background)
        car_group.clear(screen, background)
        car_group.update(screen)
        hazards.draw(screen)
        car_group.draw(screen)

        pygame.display.flip()
         
    pygame.quit()

main()
