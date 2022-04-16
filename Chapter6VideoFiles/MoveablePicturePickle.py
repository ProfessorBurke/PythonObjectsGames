"""Move an image by pressing keys."""
from typing import ClassVar
import os.path
import pickle
import io
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
    _image_file: str
    _image: pygame.Surface
    
    def __init__(self, x: float, y: float, image_file: str) -> None:
        """Initialize an instance of image at x,y."""
        self._image_file = image_file
        self._image = pygame.image.load(image_file)
        self._x = x - self._image.get_width() / 2
        self._y = y - self._image.get_height() / 2

    def __getstate__(self) -> dict:
        """Return a copy of this object's dict with image removed."""
        copy_dict: dict = self.__dict__.copy()
        if "_image" in copy_dict:
            del copy_dict["_image"]
        return copy_dict

    def __setstate__(self, pickled_dict: dict) -> None:
        """Read the object in and load the image."""
        self.__dict__ = pickled_dict
        self._image = pygame.image.load(self._image_file)

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
    _screen: pygame.Surface
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
    # Annotate variables
    file_out: io.BufferedWriter
    file_in: io.BufferedReader
    picture: MoveablePicture
    picture_mover: PictureMover
    settings: Settings
    
    # Initialize pygame.
    pygame.init()

    # Read settings and picture from file if it exists.
    if os.path.isfile("picture_mover"):
        with open("picture_mover", "rb") as file_in:
            settings = pickle.load(file_in)
            picture = pickle.load(file_in)
    else:
        settings = Settings(Settings.ARROW, (480, 480))
        picture: MoveablePicture = MoveablePicture(480/2,
                                                   480/2,
                                                   "eclipse_small.jpg")

    # Create and run the program.
    picture_mover = PictureMover(settings, picture)
    picture_mover.go()

    # Clean up resources.
    pygame.quit()

    with open("picture_mover", "wb") as file_out:
        pickle.dump(settings, file_out)
        pickle.dump(picture, file_out)

main()
