import pygame
from os import path

class Gold(pygame.sprite.Sprite):
    """A goal in the game."""

    # Annotate object-level fields
    _images: list
    _current_image: int
    _rotation_timer: int
    _disappear_timer: int
    _disappear_time: int

    def __init__(self, x: int, y: int, disappear_time: int) -> None:
        """Create a spinning coin."""
        super().__init__()
        i: int
        self._images = []
        for i in range(6):
            self._images.append(pygame.image.load(path.join("images", "coins",
                                                            "coin" + str(i) + ".png")).convert_alpha())
        self._current_image = 0
        self.image = self._images[self._current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._disappear_time = disappear_time
        self._rotation_timer = 0
        self._disappear_timer = 0             

    def update(self, gold: pygame.sprite.Group) -> None:
        """Update the spinning animation and possibly jump."""
        # Update the disappear timer and remove from group if time.
        self._disappear_timer += 1
        if self._disappear_timer % self._disappear_time == 0:
            gold.remove(self)
        else:
            # Update the spinning animation.
            self._rotation_timer += 1
            if self._rotation_timer % 3 == 0:
                self._current_image += 1
                self.image = self._images[self._current_image % len(self._images)]
                loc: tuple = self.rect.topleft
                self.rect = self.image.get_rect()
                self.rect.topleft = loc
