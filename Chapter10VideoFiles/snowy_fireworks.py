"""Demonstrate layering and an animated sprite.
   Big Ben image from https://negativespace.co/big-ben-night/
   """

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class Architecture(pygame.sprite.Sprite):

    # Annotate object-level fields

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Snowflake(pygame.sprite.Sprite):

    # Annotate object-level fields
    _dy: int

    def __init__(self, image: pygame.Surface, screen: pygame.Surface) -> None:
        """Initialize the sprite."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(int(-image.get_width() / 2),
                                        screen.get_width() + int(image.get_width() / 2))
        self.rect.top = random.randint(int(-image.get_height()/ 2),
                                       screen.get_height() + int(image.get_height() / 2))
        self._dy = random.randint(4, 10)

    def update(self, screen: pygame.Surface) -> None:
        self.rect.top += self._dy
        if self.rect.top >= screen.get_height():
            self.rect.bottom = 0
            self.rect.left = random.randint(int(-self.image.get_width() / 2),
                                        screen.get_width() + int(self.image.get_width() / 2))
            self._dy = random.randint(4, 10)

class Firework(pygame.sprite.Sprite):

    # Annotate object-level fields
    _images: list
    _counter: int
    _image_index: int

    def __init__(self, images: list, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._images = images
        self._image_index = random.randint(0, len(images) - 1)
        self.image = images[self._image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._counter = 0

    def update(self, screen: pygame.Surface) -> None:
        self._counter += 1
        if self._counter % 5 == 0:
            self._image_index += 1
            if self._image_index % len(self._images) == 0:
                self.rect.x = random.randint(-(int(self.rect.width / 2)),
                                             screen.get_width())
                self.rect.y = random.randint(-(int(self.rect.height / 2)),
                                             screen.get_height())
                self._image_index = 0
            self.image = self._images[self._image_index]

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
    big_ben_image: pygame.Surface
    snowflake_images: list
    blue_fireworks_images: list
    red_fireworks_images: list
    big_ben: Architecture
    snowflake: Snowflake
    firework: Firework
    architecture_group: pygame.sprite.Group = pygame.sprite.Group()
    snowflake_group: pygame.sprite.Group = pygame.sprite.Group()
    fireworks_group: pygame.sprite.Group = pygame.sprite.Group()
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background = pygame.Surface((WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    # Create big ben
    big_ben_image = pygame.image.load("big_ben.png").convert_alpha()
    big_ben = Architecture(big_ben_image,
                           screen.get_width() / 2,
                           screen.get_height() - big_ben_image.get_height())
    architecture_group.add(big_ben)
    # Create snow
    snowflake_images = [pygame.image.load("snowflake1.png").convert_alpha(),
                        pygame.image.load("snowflake2.png").convert_alpha(),
                        pygame.image.load("snowflake3.png").convert_alpha(),
                        pygame.image.load("snowflake4.png").convert_alpha()]
    for i in range(50):
        snowflake = Snowflake(random.choice(snowflake_images), screen)
        snowflake_group.add(snowflake)
    # Create fireworks
    blue_fireworks_images = [pygame.image.load("blue_firework0.png").convert_alpha(),
                             pygame.image.load("blue_firework1.png").convert_alpha(),
                             pygame.image.load("blue_firework2.png").convert_alpha(),
                             pygame.image.load("blue_firework3.png").convert_alpha(),
                             pygame.image.load("blue_firework4.png").convert_alpha(),
                             pygame.image.load("blue_firework5.png").convert_alpha()]
    red_fireworks_images = [pygame.image.load("red_firework0.png").convert_alpha(),
                            pygame.image.load("red_firework1.png").convert_alpha(),
                            pygame.image.load("red_firework2.png").convert_alpha(),
                            pygame.image.load("red_firework3.png").convert_alpha(),
                            pygame.image.load("red_firework4.png").convert_alpha(),
                            pygame.image.load("red_firework5.png").convert_alpha()]
    h_offset: int = int(blue_fireworks_images[0].get_width() / 2)
    v_offset: int = int(blue_fireworks_images[0].get_height() / 2)
    for i in range(3):
        firework = Firework(blue_fireworks_images, random.randint(-h_offset, screen.get_width()),
                            random.randint(-v_offset, int(screen.get_height() / 2)))
        fireworks_group.add(firework)
    for i in range(3):
        firework = Firework(red_fireworks_images, random.randint(-h_offset, screen.get_width()),
                            random.randint(-v_offset, int(screen.get_height() / 2)))
        fireworks_group.add(firework)

  
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
                    
        # Draw sprites.
        fireworks_group.clear(screen, background)
        architecture_group.clear(screen, background)
        snowflake_group.clear(screen, background)
        fireworks_group.update(screen)
        architecture_group.update(screen)
        snowflake_group.update(screen)
        fireworks_group.draw(screen)
        architecture_group.draw(screen)
        snowflake_group.draw(screen)
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
