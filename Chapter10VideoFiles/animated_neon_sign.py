"""Animate a neon sign sprite."""

# Import and initialize pygame.
import pygame
pygame.init()

class Sign(pygame.sprite.Sprite):

    # Annotate object-level fields
    _images: list
    _count: int
    _image_index: int

    def __init__(self, images: list, screen: pygame.Surface) -> None:
        """Initialize the sprite."""
        super().__init__()
        self.image = images[0]
        self._image_index = 0
        self._images = images
        self.rect = self.image.get_rect()
        x: int = screen.get_width() - images[0].get_width()
        y: int = screen.get_height() - images[0].get_height()
        self.rect.topleft= (x, y)
        self._count = 0

    def update(self, screen: pygame.Surface) -> None:
        """Every 20 updates (2/3 second), change the image."""
        self._count += 1
        if self._count % 20 == 0:
            self._image_index += 1
            self.image = self._images[self._image_index % len(self._images)]
   

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Create a neon sign."""
    # Annotate and initialize variables
    WIDTH: int = 525
    HEIGHT: int = 250
    screen: pygame.Surface
    background: pygame.Surface
    sprite: Sign
    images: list 
    group: pygame.sprite.Group = pygame.sprite.Group()
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Lights!"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((25, 25, 25))
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    images = []
    for i in range(1, 4):
        images.append(pygame.image.load("light" + str(i) + ".png").convert_alpha())
    sprite = Sign(images, screen)
    group.add(sprite)

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                    
        # Draw the sign.
        group.clear(screen, background)
        group.update(screen)
        group.draw(screen)     
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
