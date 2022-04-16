"""Collision detection between groups."""

# Imports and initialize pygame.
from typing import ClassVar
import random
import math
import pygame
pygame.init()


class Goat(pygame.sprite.Sprite):
    """A randomly snacking goat."""

    # Annotate object-level fields
    _angle: float
    _speed: int
    _timer: int
    _x: float
    _y: float
    _name: str
    _raw_image: pygame.Surface
    _max_timer: int

    def _change_rotation(self) -> None:
        """Rotate the image to match the angle."""
        self.image = pygame.transform.rotate(self._raw_image, -self._angle)
        self.rect = self.image.get_rect()
        self.rect.left = self._x
        self.rect.top = self._y
        self.mask = pygame.mask.from_surface(self.image)

    def __init__(self, screen: pygame.Surface, image: str, name: str) -> None:
        """Initialize goat with a mask."""
        pygame.sprite.Sprite.__init__(self)
        self._name = name
        self._angle = random.randint(0, 350)
        self._raw_image = pygame.image.load(image)
        self._raw_image = self._raw_image.convert_alpha()
        self.image = pygame.transform.rotate(self._raw_image, -self._angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._y = random.randint(0, screen.get_height()
                                       - self.rect.bottom)
        self._x = random.randint(0, screen.get_width()
                                        - self.rect.right)
        self.rect.top = self._y
        self.rect.right = self._x
        self._randomize()

    def get_name(self) -> str:
        return self._name
        
    def update(self, screen: pygame.Surface) -> None:
        """Move the goat."""
        if self._timer % 60 == 0:
            self._timer += random.choice([0,0,0,0,0,0,0,0,0,1])
        self._x += self._speed * math.cos(math.radians(self._angle))
        self._y += self._speed * math.sin(math.radians(self._angle))
        if self._x <= 0:
            self._x = 0
            self._angle += 10
            self._change_rotation()
        elif self._x + self.image.get_width() >= screen.get_width():
            self._x = screen.get_width() - self.image.get_width()
            self._angle += 10
            self._change_rotation()
        if self._y <= 0:
            self._y = 0
            self._angle += 10
            self._change_rotation()
        elif self._y + self.image.get_height() >= screen.get_height():
            self._y = screen.get_height() - self.image.get_height()
            self._angle += 10
            self._change_rotation()
        self.rect.top = self._y
        self.rect.left = self._x

        self._timer += 1
        if self._timer == self._max_timer:
            self._randomize()
            
    def _randomize(self) -> None:
        """Randomize goat direction and time to next change."""
        self._max_timer = random.randint(50, 150)
        self._angle += random.choice([-10, 10])
        self._speed = random.randint(0, 2)
        self._timer = 0
        self._change_rotation()

class Weed(pygame.sprite.Sprite):
    """A non-moving weed."""

    # Annotate and define class-level field
    _image: ClassVar[pygame.Surface] = pygame.image.load("weed.png")

    # Annotate object-level fields
    _name: str

    def get_name(self) -> str:
        return self._name

    def __init__(self, screen: pygame.Surface, name: str) -> None:
        """Initialize a weed with a mask."""
        pygame.sprite.Sprite.__init__(self)
        self._name = name
        self.image = Weed._image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
    goat: Goat
    goats: pygame.sprite.Group
    weed: Weed
    weeds: pygame.sprite.Group
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Just watch the goats")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((102, 164, 115))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    # Make goats, weeds, and groups
    goats = pygame.sprite.Group()
    goats.add(Goat(screen, "black_and_tan_goat.png", "Jumbuck"),
              Goat(screen, "brown_goat.png", "Clover"),
              Goat(screen, "spotty_goat.png", "Pan"))
    weeds = pygame.sprite.Group()
    
    for i in range(30):
        weeds.add(Weed(screen, "weed " + str(i)))

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True                
 
        # Check for collisions
        eaten = pygame.sprite.groupcollide(goats,
                                                weeds, False, True,
                                                pygame.sprite.collide_mask)
        for goat in eaten:
            for weed in eaten[goat]:
                print(goat.get_name() + " ate " + weed.get_name())
                
        # Draw to the screen and show.
        goats.clear(screen, background)
        weeds.clear(screen, background)
        goats.update(screen)
        weeds.draw(screen)
        goats.draw(screen)

        pygame.display.flip()
         
    pygame.quit()

main()
