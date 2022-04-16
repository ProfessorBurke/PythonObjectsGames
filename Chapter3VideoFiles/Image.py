import pygame

class Image():
    """A class for creating a moveable pygame image.

       Public methods:  __init__, select, deselect, set_upper_left,
                        set_center, contained_in, draw

    """

    # Annotate object-level fields
    _image: pygame.Surface
    _x: int
    _y: int
    _selected: bool

    def __init__(self, file_name: str, x: int = 0, y: int = 0) -> None:
        """Initialize an Image object from parameters."""
        self._x = x
        self._y = y
        self._selected = False
        self._image = pygame.image.load(file_name)
        self._image.convert()

    def select(self) -> None:
        """Select this image."""
        self._selected = True

    def deselect(self) -> None:
        """Deselect this image."""
        self._selected = False
    
    def set_upper_left(self, left: int, top: int) -> None:
        """Move the top left of image to (x,y)."""
        self._x = left
        self._y = top

    def set_center(self, center_x: int, center_y: int) -> None:
        """Move the center of image to (x,y)."""
        self._x = center_x - self._image.get_width() // 2
        self._y = center_y - self._image.get_height() // 2

    def contained_in(self, x: int, y: int) -> bool:
        """Return True if x,y is within image, False otherwise."""
        return (self._x <= x and x <= self._x + self._image.get_width()
            and self._y <= y and y <= self._y + self._image.get_height())

    def draw(self, surface: pygame.Surface) -> None:
        """Draw image to surface showing as either selected or deselected."""
        if self._selected:
            surf = pygame.Surface((self._image.get_width() + 4, self._image.get_height() + 4))
            surf.fill((255, 255, 255))
            surface.blit(surf, (self._x-2, self._y-2))
        surface.blit(self._image, (self._x, self._y))
        
        
