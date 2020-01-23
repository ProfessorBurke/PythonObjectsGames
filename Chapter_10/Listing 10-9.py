"""Tiled background sprite with wall collision detection."""

# Imports and initialize pygame.
import pygame
import io
import math
pygame.init()

# Constants
LEFT: int = 0
RIGHT: int = 1
UP: int = 2
DOWN: int = 3
NOT_MOVING: int = -1

class Brick(pygame.sprite.Sprite):
    """Just another brick..."""

    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        """Create an invisible sprite."""
        super().__init__()
        self.image = pygame.Surface((width, length))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Background(pygame.sprite.Sprite):
    """A tile-based background."""

    # Annotate object-level fields
    _bricks: list

    def __init__(self, tile_files: list, terrain_file: str, bricks: list) -> None:
        """Load map and build Surface."""
        # Annotate and initialize local variables
        name: str
        line: str
        tile_size: int
        width: int
        height: int
        x: int = 0
        y: int = 0
        terrain: io.TextIOWrapper
        # Superclass init.
        super().__init__()
        # Load the images to pygame Surfaces.
        tiles: list = []
        for name in tile_files:
            tiles.append(pygame.image.load(name).convert())
        # Load the terrain map into a 2D list.
        terrain_map: list = []
        with open(terrain_file) as terrain:
            line = terrain.readline()
            while line != "":
                terrain_map.append(line.split())
                line = terrain.readline()
        # Calculate the size of the Surface and create.
        tile_size = tiles[0].get_width()
        width = len(terrain_map[0]) * tile_size
        height = len(terrain_map) * tile_size
        self.image = pygame.Surface((width, height)) 
        # Blit the images to the Surface.
        # Create a Block if necessary.
        self._bricks = []
        for row in terrain_map:
            for i in row:
                self.image.blit(tiles[int(i)], (x, y))
                if int(i) in bricks:
                    self._bricks.append(Brick(x, y, tile_size, tile_size))
                x += tile_size
            y += tile_size
            x = 0
        # Complete initialization
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def get_bricks(self) -> list:
        """Return the bricks."""
        return self._bricks

class Penguin(pygame.sprite.Sprite):
    """A player-controlled character."""

    # Annotate object-level fields
    _raw_image: pygame.Surface
    _speed: int
    _angle: int

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self._raw_image = pygame.image.load("top_penguin.png")
        self._raw_image = self._raw_image.convert_alpha()
        self.image = self._raw_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, screen.get_height() / 2 - self.rect.height / 2)
        self._speed = 5
        self._angle = 0

    def move(self, screen: pygame.Surface, 
             direction: int) -> None:
        """Move in direction."""
        if direction == LEFT:
            self._angle = 180
            self.image = pygame.transform.rotate(self._raw_image, 180)
            self.rect.left -= self._speed
            if self.rect.left < 0:
                self.rect.left = 0
        elif direction == RIGHT:
            self._angle = 0
            self.image = self._raw_image
            self.rect.left += self._speed
            if self.rect.right > screen.get_width():
                self.rect.right = screen.get_width()
        elif direction == UP:
            self._angle = 270
            self.image = pygame.transform.rotate(self._raw_image, 90)
            self.rect.top -= self._speed
            if self.rect.top < 0:
                self.rect.top = 0
        elif direction == DOWN:
            self._angle = 90
            self.image = pygame.transform.rotate(self._raw_image, -90)
            self.rect.top += self._speed
            if self.rect.bottom > screen.get_height():
                self.rect.bottom = screen.get_height()

    def backup(self) -> None:
        """Back up one unit displacement vector."""
        # Calculate a unit vector
        dx: float = -math.cos(math.radians(self._angle))  
        dy: float = -math.sin(math.radians(self._angle)) 
        # Add to rectangle
        self.rect.left += dx
        self.rect.top += dy        
            
def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """The arrow keys move the penguin or scroll."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: ScrollingBackground
    bkgd_group: pygame.sprite.Group
    bricks: pygame.sprite.Group
    penguin: Penguin
    penguin_group: pygame.sprite.Group
    user_quit: bool = False
    e: pygame.event.Event
    direction: int = NOT_MOVING
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Terrain collisions")
    image_files: list = ["ice_block.jpg", "ice_wall.jpg"]
    background = Background(image_files, "small_ice_castle.txt", [0])
    bkgd_group = pygame.sprite.Group(background)
    bricks = pygame.sprite.Group(background.get_bricks())
    penguin = Penguin(screen)
    penguin_group = pygame.sprite.Group(penguin)
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                # Process movement arrow keys.
                if e.__dict__["key"] == pygame.K_LEFT:
                    direction = LEFT
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    direction = RIGHT
                elif e.__dict__["key"] == pygame.K_UP:
                    direction = UP
                elif e.__dict__["key"] == pygame.K_DOWN:
                    direction = DOWN
            elif e.type == pygame.KEYUP:
                if (not pygame.key.get_pressed()[pygame.K_LEFT] 
                        and not pygame.key.get_pressed()[pygame.K_RIGHT]
                        and not pygame.key.get_pressed()[pygame.K_UP]
                        and not pygame.key.get_pressed()[pygame.K_DOWN]):
                    direction = NOT_MOVING

        # Move the penguin.
        penguin_group.clear(screen, background.image)
        penguin.move(screen, direction)
        # Check for collisions.
        while pygame.sprite.spritecollide(penguin, bricks, False):
            penguin.backup()
        # Redraw and show.
        bkgd_group.draw(screen)
        penguin_group.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
