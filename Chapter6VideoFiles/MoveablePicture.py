"""Move an image by pressing keys."""
from typing import ClassVar
import pygame

class MoveablePicture():
    """An image that can be moved.

       Public methods: __init__, draw, move
    """
    #Annotate and initialize class-level fields
    UP: ClassVar[int] = 0
    DOWN: ClassVar[int] = 1
    LEFT: ClassVar[int] = 2
    RIGHT: ClassVar[int] = 3

    # Annotate object-level fields
    _x: float
    _y: float
    _image: pygame.Surface
    
    def __init__(self, x: float, y: float, image: pygame.Surface) -> None:
        """Initialize an instance of image at x,y."""
        self._x = x
        self._y = y
        self._image = image

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the image on the surface."""
        surface.blit(self._image, (self._x, self._y))

    def move(self, direction: int) -> None:
        """Move the image 5 pixels in direction."""
        if direction == MoveablePicture.UP:
            self._y -= 5
        elif direction == MoveablePicture.DOWN:
            self._y += 5
        elif direction == MoveablePicture.LEFT:
            self._x -= 5
        elif direction == MoveablePicture.RIGHT:
            self._x += 5

class Settings():
    """Settings for the program.

       Public methods: __init__, get_keys, get_size
    """
    # Annotate and initialize class-level fields
    ARROW: ClassVar[tuple] = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    ASDW: ClassVar[tuple] = (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    
    # Annotate object-level fields
    _key_settings: tuple
    _size: tuple

    def __init__(self, key_settings, size) -> None:
        self._key_settings = key_settings
        self._size = size

    def get_keys(self) -> tuple:
        return self._key_settings

    def get_size(self) -> tuple:
        return self._size

class PictureMover():

    # Annotate object-level fields
    _picture: MoveablePicture
    _sceen: pygame.Surface
    _background: pygame.Surface
    _keys: tuple

    def __init__(self, settings: Settings, picture: MoveablePicture) -> None:
        """Initialize from settings, create window."""
        # Annotate variables
        size: tuple
        # Create the window.
        size = settings.get_size()
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Press keys to move the picture")
        self._background = pygame.Surface(size)
        ## Enable key hold -- turned off for this version.
        ## pygame.key.set_repeat(1, 50)
        # Read in the picture.
        self._keys = settings.get_keys()
        self._picture = picture
        
    def go(self) -> None:
        """Create a window with an image that can be moved."""
        # Annotate and initialize variables
        user_quit: bool = False
        clock: pygame.time.Clock = pygame.time.Clock()
        event: pygame.event.Event
            
        # Run until the user closes the window.
        while not user_quit:
            # Loop 30 times per second
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    user_quit = True
                elif event.type == pygame.KEYDOWN:
                    # Process arrow key events by moving picture
                    key = event.__dict__["key"]
                    if key == self._keys[0]:
                        self._picture.move(MoveablePicture.UP)
                    elif key == self._keys[1]:
                        self._picture.move(MoveablePicture.DOWN)
                    elif key == self._keys[2]:
                        self._picture.move(MoveablePicture.LEFT)
                    elif key == self._keys[3]:
                        self._picture.move(MoveablePicture.RIGHT)
                        
            # Draw the background and picture               
            self._screen.blit(self._background,(0,0))
            self._picture.draw(self._screen)
            pygame.display.flip()

def main():
    # Initialize pygame and the settings.
    pygame.init()
    settings = Settings(Settings.ARROW, (480, 480))

    # Create a picture to move.
    image: pygame.Surface = pygame.image.load("eclipse_small.jpg")
    picture: MoveablePicture = MoveablePicture(480/2 - image.get_width() / 2,
                                               480/2 - image.get_height() / 2, image)

    # Create and run the program.
    picture_mover = PictureMover(settings, picture)
    picture_mover.go()

    # Clean up resources.
    pygame.quit()

main()
