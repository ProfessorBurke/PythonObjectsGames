"""Scorekeeper sprite and stubs."""

# Import and initialize pygame.
import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    """Stub for player."""
    def get_health(self) -> int:
        return 5
    def get_num_spheres(self) -> int:
        return 2

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
        super().__init__()
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
            self.image.fill((222, 237, 244))
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
    """Move an image randomly on the screen."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    scorekeeper: Scorekeeper
    sprites: pygame.sprite.Group
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Scorekeeper")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    screen.blit(background, (0, 0))
    scorekeeper = Scorekeeper(Player(), Level())
    sprites = pygame.sprite.Group(scorekeeper)
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                
        # Draw to the screen and show.
        sprites.clear(screen, background)
        sprites.update(screen)
        sprites.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
