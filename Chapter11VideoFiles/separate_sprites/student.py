import pygame
import math

class Student(pygame.sprite.Sprite):

    # Annotate class-level constants
    UP: int = 1
    DOWN: int = 3
    LEFT: int = 2
    RIGHT: int = 0
    STOP: int = 4

    # Annotate object-level fields
    _dx: int
    _dy: int
    _speed: int
    _face_right: pygame.Surface
    _coins: int

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._face_right = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 0
        self._dy = 0
        self._speed = 5
        self._coins = 0

    def get_coins(self) -> int:
        """Return the number of coins."""
        return self._coins

    def add_coins(self, num_coins: int) -> None:
        """Add num_coins to coins total."""
        self._coins += num_coins

    def move(self, direction: int) -> None:
        self._dx = 0
        self._dy = 0
        if direction != Student.STOP:
            rotation: int = direction * 90
            x: int = self.rect.centerx
            y: int = self.rect.centery
            self.image = pygame.transform.rotate(self._face_right, rotation)
            self.rect.centerx = x
            self.rect.centery = y
            if direction == Student.LEFT:
                self._dx = -self._speed
            elif direction == Student.RIGHT:
                self._dx = self._speed
            if direction == Student.UP:
                self._dy = -self._speed
            elif direction == Student.DOWN:
                self._dy = self._speed

    def through_doorway(self, screen: pygame.Surface) -> None:
        """Move through a doorway into the next level."""
        # Moving left
        if self._dx == -self._speed:
            self.rect.right = screen.get_width() - 50
        # Moving right
        elif self._dx == self._speed:
            self.rect.left = 50
        # Moving up
        elif self._dy == -self._speed:
            self.rect.bottom = screen.get_height() - 50
        # Moving down
        elif self._dy == self._speed:
            self.rect.top = 50

    def update(self, bricks: pygame.sprite.Group) -> None:
        self.rect.top += self._dy
        self.rect.left += self._dx
        while pygame.sprite.spritecollide(self, bricks, False):
            # Calculate a unit vector
            distance: float = math.sqrt(self._dx ** 2 + self._dy ** 2)
            if distance != 0:
                x: float = self._dx / distance
                y: float = self._dy / distance
                # Backup
                self.rect.top -= y
                self.rect.left -= x
