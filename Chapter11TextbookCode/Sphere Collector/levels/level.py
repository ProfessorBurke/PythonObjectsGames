import pygame
pygame.init()

from sprites.enemy import Enemy
from sprites.sphere import Sphere

class Level():
    """A level in the game."""

    # Annotate object-level fields.
    _level_number: int
    _num_enemies: int
    _size_enemies: int
    _num_spheres: int
    _size_spheres: int

    def __init__(self, num: int, enemy_num: int, enemy_size: int, sphere_num: int,
                 sphere_size: int) -> None:
        """Initialize from parameters."""
        self._level_number = num
        self._num_enemies = enemy_num
        self._size_enemies = enemy_size
        self._num_spheres = sphere_num
        self._size_spheres = sphere_size

    def get_enemies(self, screen: pygame.Surface) -> pygame.sprite.Group:
        """Return a group of enemies."""
        enemies: pygame.sprite.Group = pygame.sprite.Group()
        i: int
        for i in range(self._num_enemies):
            enemies.add(Enemy(screen, self._size_enemies))
        return enemies

    def get_spheres(self, screen: pygame.Surface) -> pygame.sprite.Group:
        """Return a group of spheres."""
        spheres: pygame.sprite.Group = pygame.sprite.Group()
        i: int
        for i in range(self._num_spheres):
            spheres.add(Sphere(screen, self._size_spheres))
        return spheres
        
    def get_level(self) -> int:
        """Return the number of this level."""
        return self._level_number
    
    def get_total_spheres(self) -> int:
        """Return the total number of spheres."""
        return self._num_spheres
