"""Platform scroller."""

# Imports and initialize pygame.
import pygame
import io
import math
pygame.init()

# Constants
LEFT: int = 0
RIGHT: int = 1
UP: int = 2
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

    def move(self, dx: int, dy: int) -> None:
        """Move by dx and dy."""
        self.rect.left += dx
        self.rect.right += dy

class ScrollingBackground(pygame.sprite.Sprite):
    """A tile-based scrolling background."""

    # Annotate object-level fields
    _speed: int
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
        self._speed = 5

    def scroll(self, direction: int, screen: pygame.Surface) -> None:
        """Move left, right, or not at all."""
        # Annotate and initialize local variable
        left: int = self.rect.left
        # Scroll image and bricks.
        if direction == LEFT:
            self.rect.left += self._speed
            if self.rect.left > 0:
                self.rect.left = 0
            for brick in self._bricks:
                brick.move(self.rect.left - left, 0)
        elif direction == RIGHT:
            self.rect.left -= self._speed
            if self.rect.right < screen.get_width():
                self.rect.right = screen.get_width()
            for brick in self._bricks:
                brick.move(self.rect.left - left, 0)

    def can_scroll(self, screen: pygame.Surface, direction: int) -> bool:
        """Return True if can scroll in direction."""
        scroll: bool = False
        if direction == LEFT and self.rect.left < 0:
            scroll = True
        elif direction == RIGHT and self.rect.right > screen.get_width():
            scroll = True
        return scroll

    def get_bricks(self) -> list:
        """Return the bricks."""
        return self._bricks

class Penguin(pygame.sprite.Sprite):
    """A player-controlled character."""

    # Annotate object-level fields
    _raw_image: pygame.Surface
    _dx: float
    _dy: float
    _facing: int
    _x: float
    _y: float

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize from parameters."""
        super().__init__()
        self._raw_image = pygame.image.load("tiny_penguin.png")
        self._raw_image = self._raw_image.convert_alpha()
        self.image = self._raw_image
        self.rect = self.image.get_rect()
        self._x = 0
        self._y = screen.get_height() - 40 - self.rect.height
        self.rect.topleft = (self._x, self._y)
        self._dx = 0
        self._dy = 0
        self._facing = RIGHT

    def on_ground(self, bricks) -> bool:
        """Return True if the sprite is on a solid brick."""
        on: bool = False
        self.rect.top += 1
        if pygame.sprite.spritecollide(self, bricks, False):
            on = True
        self.rect.top -= 1
        return on

    def process_move_command(self, move_command: int,
                             bricks: pygame.sprite.Group) -> None:
        """Process a command from the user."""
        # If it's on the ground, it can move or jump.
        if self.on_ground(bricks):
            self._dy = 0
            if move_command == LEFT:
                self._dx = -5
                self._facing = LEFT
                self.image = pygame.transform.flip(self._raw_image, True, False)
            elif move_command == RIGHT:
                self._dx = 5
                self._facing = RIGHT
                self.image = self._raw_image
            elif move_command == UP:
                self._dy = -50
                if self._facing == LEFT:
                    self._dx = -5
                else:
                    self._dx = 5
        # Stop moving in the x direction.
        if move_command == NOT_MOVING:
            self._dx = 0

            
    def move_x(self, screen: pygame.Surface, threshold: int,
             background: ScrollingBackground) -> int:
        """Attempt to move, return True if moved."""
        moved: bool = False
        scroll_dir: int = NOT_MOVING

        # Adjust x according to dx.
        if self._dx < 0:
            can_scroll = background.can_scroll(screen, LEFT)
            if not(can_scroll and self.rect.left < threshold):
                self._x += self._dx
                if self._x < 0:
                    self._x = 0
                self.rect.left = self._x
            else:
                scroll_dir = LEFT
        elif self._dx > 0:
            can_scroll = background.can_scroll(screen, RIGHT)
            if not(can_scroll and self.rect.right > screen.get_width() - threshold):
                self._x += self._dx
                if self._x > screen.get_width() - self.rect.width:
                    self._x = screen.get_width() - self.rect.width
                self.rect.left = self._x
            else:
                scroll_dir = RIGHT
                
        return scroll_dir

    def backup_x(self) -> None:
        """Back up one unit displacement vector."""
        # Calculate a unit vector
        dx: float = -(self._dx / (math.sqrt(self._dx**2 + self._dy**2)))  
        # Add to coordinates
        self._x += dx
        self.rect.topleft = (self._x, self._y)

    def move_y(self, screen: pygame.Surface, bricks: pygame.sprite.Group):
        """Move in the y coordinate."""
        # If it's not on the ground, it's falling.
        if not self.on_ground(bricks):
            # Start freefall
            if round(self._dy) == 0:
                self._dy = 1
            # Going up
            elif self._dy < 0:
                self._dy *= .4
            # Going down
            else:
                self._dy += 2

        # Adjust y according to dy.
        self._y += self._dy
        self.rect.top = self._y

    def backup_y(self) -> None:
        """Back up one unit displacement vector."""
        # Calculate a unit vector 
        dy: float = -(self._dy / (math.sqrt(self._dx**2 + self._dy**2)))
        # Add to coordinates
        self._y += dy
        self.rect.topleft = (self._x, self._y)

            
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
    scroll_threshold: int = 100
    direction: int = NOT_MOVING
    scroll_dir: int = NOT_MOVING
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Scrolling Background")
    image_files: list = ["ice_block.jpg", "ice_wall.jpg"]
    background = ScrollingBackground(image_files, "ice_castle.txt", [0])
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
                    penguin.process_move_command(LEFT, bricks)
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    penguin.process_move_command(RIGHT, bricks)
                elif e.__dict__["key"] == pygame.K_UP:
                    penguin.process_move_command(UP, bricks)
            elif e.type == pygame.KEYUP:
                if (not pygame.key.get_pressed()[pygame.K_LEFT] 
                        and not pygame.key.get_pressed()[pygame.K_RIGHT]
                        and not pygame.key.get_pressed()[pygame.K_UP]):
                    penguin.process_move_command(NOT_MOVING, bricks)

        # Move the penguin or the background.
        penguin_group.clear(screen, background.image)
        # Move and check for collisions.
        scroll_dir = penguin.move_x(screen, scroll_threshold, background)
        background.scroll(scroll_dir, screen)
        while pygame.sprite.spritecollide(penguin, bricks, False):
            penguin.backup_x()
        penguin.move_y(screen, bricks)
        while pygame.sprite.spritecollide(penguin, bricks, False):
            penguin.backup_y()

        # Redraw and show.
        bkgd_group.draw(screen)
        penguin_group.draw(screen)
        pygame.display.flip()
         
    pygame.quit()

main()
