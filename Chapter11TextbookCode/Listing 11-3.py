"""Scorekeeper sprite and stubs."""

from typing import ClassVar
import random

# Import and initialize pygame.
import pygame
pygame.init()

class Enemy(pygame.sprite.Sprite):
    """A randomly moving enemy."""

    # Annotate and initialize class-level field
    MAX_TIME: ClassVar[int] = 120

    # Annotate object-level fields
    _dx: int
    _dy: int
    _timer: int

    def __init__(self, screen: pygame.Surface, size: int) -> None:
        """Set sprite to initial state."""
        super().__init__()
        self._dx = random.randint(1, 7)
        self._dy = random.randint(0, 5)
        self._timer = random.randint(0, Enemy.MAX_TIME - 1)
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, screen.get_width() - size)
        self.rect.top = random.randint(0, screen.get_height() - size)

    def update(self, screen) -> None:
        """Move and possibly reset dx and dy."""
        # Randomize speed and direction each MAX_TIME.
        self._timer += 1
        if self._timer == Enemy.MAX_TIME:
            self._dx = random.randint(1, 7)
            self._dy = random.randint(0, 5)
            self._timer = 0
        # Move and wrap at boundaries.
        self.rect.left += self._dx
        self.rect.top += self._dy
        if self.rect.right < 0:
            self.rect.left = screen.get_width()
        elif self.rect.left > screen.get_width():
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = screen.get_height()
        elif self.rect.top > screen.get_height():
            self.rect.bottom = 0

    def change_location(self, screen: pygame.Surface) -> None:
        """Change to a new random location."""
        self.rect.left = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.top = random.randint(0, screen.get_height() - self.rect.height)   

class Sphere(pygame.sprite.Sprite):
    """A non-moving goal."""

    def __init__(self, screen: pygame.Surface, size: int) -> None:
        """Set sprite to initial state."""
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (213, 244, 255), (size // 2, size // 2), size // 2)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, screen.get_width() - size)
        self.rect.top = random.randint(0, screen.get_height() - size)
    
class Player(pygame.sprite.Sprite):
    """Player motion is controlled by the arrow keys."""

    # Annotate and initialize class-level fields
    STOP: ClassVar[int] = -1
    LEFT: ClassVar[int] = 0
    RIGHT: ClassVar[int] = 1
    UP: ClassVar[int] = 2
    DOWN: ClassVar[int] = 3

    # Annotate object-level fields
    _health: int
    _spheres: int
    _dx: int
    _dy: int

    def __init__(self, screen: pygame.Surface) -> None:
        """Set sprite to initial state."""
        super().__init__()
        self._health = 5
        self._spheres = 0
        self._dx = 0
        self._dy = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = (screen.get_width() - self.rect.width) / 2
        self.rect.top = (screen.get_height() - self.rect.height) / 2

    def update(self, screen: pygame.Surface) -> None:
        """Update sprite location."""
        self.rect.left += self._dx
        self.rect.top += self._dy
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()

    def move(self, direction: int) -> None:
        """Set dx or dy."""
        self._dx = 0
        self._dy = 0
        if direction == Player.LEFT:
            self._dx = -5
        elif direction == Player.RIGHT:
            self._dx = 5
        elif direction == Player.UP:
            self._dy = -5
        elif direction == Player.DOWN:
            self._dy = 5

    def reset_location(self, screen: pygame.Surface) -> None:
        """Rest to screen center."""
        self.rect.left = (screen.get_width() - self.rect.width) / 2
        self.rect.top = (screen.get_height() - self.rect.height) / 2

    def lose_health(self) -> bool:
        """Decrement health, return True if still alive."""
        self._health -= 1
        return self._health > 0

    def add_sphere(self) -> None:
        """Add to spheres score."""
        self._spheres += 1
    
    def get_health(self) -> int:
        """Return current health value."""
        return self._health
    
    def get_num_spheres(self) -> int:
        """Return current sphere value."""
        return self._spheres

class Level():
    """Stub for level."""
    def get_level(self) -> int:
        return 1
    def get_total_spheres(self) -> int:
        return 3

class Scorekeeper(pygame.sprite.Sprite):
    """Responsible for displaying an updated score."""

    # Annotate object-level fields
    _player: Player
    _level: Level
    _font: pygame.font.Font

    def __init__(self, player: Player, level: Level) -> None:
        """Initialize from parameters."""
        pygame.sprite.Sprite.__init__(self)
        self._player = player
        self._level = level
        if pygame.font:
            self._font = pygame.font.SysFont("Bauhaus 93", 24)
        self.image = pygame.Surface((0, 0)) 
        self.rect = self.image.get_rect()

    def update(self, screen: pygame.Surface) -> None:
        """Get information from player, level and render."""
        health: int = self._player.get_health()
        spheres: int = self._player.get_num_spheres()
        level: int = self._level.get_level()
        total_spheres: int = self._level.get_total_spheres()
        if pygame.font:
            level_surf: pygame.Surface = self._font.render("Level " + str(level), True, (0, 0, 0))
            health_surf: pygame.Surface = self._font.render("Health " + str(health), True, (0, 0, 0))
            spheres_surf: pygame.Surface = self._font.render("Spheres " + str(spheres) +
                                                             "/" + str(total_spheres), True, (0, 0, 0))
            self.image = pygame.Surface((screen.get_width(), self._font.get_height()))
            self.image.fill((200, 200, 200))
            self.image.blit(level_surf, (0, 0))
            self.image.blit(spheres_surf, (screen.get_width() - spheres_surf.get_width(), 0))
            self.image.blit(health_surf, ((screen.get_width() - health_surf.get_width()) / 2, 0))
            self.rect = self.image.get_rect()
        else:
            pygame.display.set_caption("Level " + str(level) + " Health " + str(health)
                               + " Spheres " + str(spheres) + "/" + str(total_spheres))

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Sphere capture game with enemies."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    game_over: bool = False
    e: pygame.event.Event
    scorekeeper: Scorekeeper
    player: Player
    sphere: Sphere
    enemies: pygame.sprite.Group
    sprites: pygame.sprite.Group
    spheres: pygame.sprite.Group
    collected_spheres: list
    collided_enemies: list
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Sphere Collector")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((200, 200, 200))
    screen.blit(background, (0, 0))
    player = Player(screen)
    scorekeeper = Scorekeeper(player, Level())
    sprites = pygame.sprite.Group(scorekeeper, player)
    enemies = pygame.sprite.Group()
    spheres = pygame.sprite.Group()
    for i in range(3):
        enemies.add(Enemy(screen, 20))
    for i in range(3):
        spheres.add(Sphere(screen, 40))

    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Process arrow keys by changing direction.
            elif e.type == pygame.KEYDOWN and not game_over:
                if e.__dict__["key"] == pygame.K_LEFT:
                    player.move(Player.LEFT)
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    player.move(Player.RIGHT)
                elif e.__dict__["key"] == pygame.K_UP:
                    player.move(Player.UP)
                elif e.__dict__["key"] == pygame.K_DOWN:
                    player.move(Player.DOWN)
            # Process keys up as stopping.
            elif e.type == pygame.KEYUP and not game_over:
                if (not pygame.key.get_pressed()[pygame.K_LEFT] 
                        and not pygame.key.get_pressed()[pygame.K_RIGHT]
                        and not pygame.key.get_pressed()[pygame.K_UP]
                        and not pygame.key.get_pressed()[pygame.K_DOWN]):
                    player.move(Player.STOP)

        if not game_over:
            # Check for collision with enemies.
            collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
            # Reset locations and set game_over if player at zero lives.
            for enemy in collided_enemies:
                enemy.change_location(screen)
                if player.lose_health():
                    player.reset_location(screen)
                else:
                    game_over = True

            # Check for collision with spheres.
            collected_spheres = pygame.sprite.spritecollide(player, spheres, True)
            for sphere in collected_spheres:
                player.add_sphere()
                
        # Draw to the screen and show.
        sprites.clear(screen, background)
        spheres.clear(screen, background)
        enemies.clear(screen, background)
        sprites.update(screen)
        enemies.update(screen)
        sprites.draw(screen)
        spheres.draw(screen)
        enemies.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
