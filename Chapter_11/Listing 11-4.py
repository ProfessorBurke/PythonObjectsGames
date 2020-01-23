"""Sphere collector game."""

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
        pygame.sprite.Sprite.__init__(self)
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
        pygame.sprite.Sprite.__init__(self)
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
        pygame.sprite.Sprite.__init__(self)
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

    def level_up(self, screen: pygame.Surface) -> None:
        """Increment health by one, reset loc and spheres."""
        self._health += 1
        self._spheres = 0
        self.reset_location(screen)

    def reset(self, screen: pygame.Surface) -> None:
        """Reset to starting state."""
        self._health = 5
        self._spheres = 0
        self.reset_location(screen)
        self._dx = 0
        self._dy = 0

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

class Scorekeeper(pygame.sprite.Sprite):
    """Responsible for displaying an updated score."""

    # Annotate object-level fields
    _player: Player
    _level: Level
    _font: pygame.font.Font
    _demo: bool

    def __init__(self, player: Player, level: Level) -> None:
        """Initialize from parameters."""
        pygame.sprite.Sprite.__init__(self)
        self._player = player
        self._level = level
        self._demo = False
        if pygame.font:
            self._font = pygame.font.SysFont("Bauhaus 93", 24)
        self.image = pygame.Surface((0, 0)) 
        self.rect = self.image.get_rect()

    def level_up(self, level: Level) -> None:
        """Set to new level."""
        self._level = level

    def demo(self, over: bool) -> None:
        """Set game over status."""
        self._demo = over

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
            if self._demo:
                self.image.set_alpha(100)
            self.image.blit(level_surf, (0, 0))
            self.image.blit(spheres_surf, (screen.get_width() - spheres_surf.get_width(), 0))
            self.image.blit(health_surf, ((screen.get_width() - health_surf.get_width()) / 2, 0))
            self.rect = self.image.get_rect()
        else:
            pygame.display.set_caption("Level " + str(level) + " Health " + str(health)
                               + " Spheres " + str(spheres) + "/" + str(total_spheres))

class Message(pygame.sprite.Sprite):
    """A message centered in the screen."""
 
    def __init__(self) -> None:
        """Initialize from parameters."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((0, 0)) 
        self.rect = self.image.get_rect()

    def set_message(self, message: str, screen: pygame.Surface) -> bool:
        """Change to new message."""
        # Annotate and initialize variables
        too_long: bool = True
        font: pygame.Font
        size: int = 38
        
        if pygame.font:
            while too_long and size >= 10:
                size -= 2
                font = pygame.font.SysFont("Bauhaus 93", size)
                too_long = font.size(message)[0] > screen.get_width()
            if size >= 10:
                self.image = font.render(message, True, (0, 0, 0))
                self.rect = self.image.get_rect()
                self.rect.left = (screen.get_width() - self.rect.width) / 2
                self.rect.top = (screen.get_height() - self.rect.height) / 2
        return self.rect.width > 0


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
    demo: bool = False
    e: pygame.event.Event
    scorekeeper: Scorekeeper
    player: Player
    sphere: Sphere
    message: Message
    enemies: pygame.sprite.Group
    sprites: pygame.sprite.Group
    spheres: pygame.sprite.Group
    collected_spheres: list
    collided_enemies: list
    levels: list
    current_level: int = 0
    i: int
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Sphere Collector")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((200, 200, 200))
    screen.blit(background, (0, 0))
    player = Player(screen)
    levels = [Level(1, 3, 20, 3, 40), Level(2, 4, 30, 4, 30),
              Level(3, 5, 40, 5, 20)]
    scorekeeper = Scorekeeper(player, levels[current_level])
    message = Message()
    sprites = pygame.sprite.Group(scorekeeper, player, message)
    enemies = levels[current_level].get_enemies(screen)
    spheres = levels[current_level].get_spheres(screen)
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Process arrow keys by changing direction.
            elif e.type == pygame.KEYDOWN and not demo:
                if e.__dict__["key"] == pygame.K_LEFT:
                    player.move(Player.LEFT)
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    player.move(Player.RIGHT)
                elif e.__dict__["key"] == pygame.K_UP:
                    player.move(Player.UP)
                elif e.__dict__["key"] == pygame.K_DOWN:
                    player.move(Player.DOWN)
            elif e.type == pygame.KEYDOWN and demo:
                if e.__dict__["key"] == pygame.K_SPACE:
                    # Start the game over
                    demo = False
                    scorekeeper.demo(False)
                    message.set_message("", screen)
                    current_level = 0
                    enemies.clear(screen, background)
                    spheres.clear(screen, background)
                    enemies = levels[current_level].get_enemies(screen)
                    spheres = levels[current_level].get_spheres(screen)
                    player.reset(screen)
                    scorekeeper.level_up(levels[current_level])

            # Process keys up as stopping.
            elif e.type == pygame.KEYUP:
                if (not pygame.key.get_pressed()[pygame.K_LEFT] 
                        and not pygame.key.get_pressed()[pygame.K_RIGHT]
                        and not pygame.key.get_pressed()[pygame.K_UP]
                        and not pygame.key.get_pressed()[pygame.K_DOWN]):
                    player.move(Player.STOP)

        if not demo:
            # Check for collision with enemies.
            collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
            # Reset locations and set demo if player at zero lives.
            for enemy in collided_enemies:
                enemy.change_location(screen)
                if not demo and player.lose_health():
                    player.reset_location(screen)
                else:
                    demo = True
                    scorekeeper.demo(True)
                    message.set_message("Space bar to play", screen)

            # Check for collision with spheres.
            collected_spheres = pygame.sprite.spritecollide(player, spheres, True)
            for sphere in collected_spheres:
                player.add_sphere()
                if player.get_num_spheres() == levels[current_level].get_total_spheres():
                    current_level += 1
                    if current_level < len(levels):
                        scorekeeper.level_up(levels[current_level])
                        enemies.clear(screen, background)
                        spheres.clear(screen, background)
                        enemies = levels[current_level].get_enemies(screen)
                        spheres = levels[current_level].get_spheres(screen)
                        player.level_up(screen)
                    else:
                        demo = True
                        scorekeeper.demo(True)
                        message.set_message("Space bar to play", screen)
               
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
