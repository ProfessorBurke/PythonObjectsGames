"""Add the program description here."""

# Import and initialize pygame.
import pygame
pygame.init()

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

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._face_right = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 0
        self._dy = 0
        self._speed = 2

    def move(self, direction: int) -> None:
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
        else:
            self._dx = 0
            self._dy = 0

    def update(self, screen: pygame.Surface) -> None:
        self.rect.top += self._dy
        self.rect.left += self._dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
        elif self.rect.top < 0:
            self.rect.top = 0
   

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def make_background(image_files: list, terrain_file: str) -> pygame.Surface:
    """Create and return a background Surface according to
       the terrain map and composed of image_files images.
       Assumes at least one image and at least one line of terrain."""
    # Annotate variables
    name: str
    line: str
    tile_size: int
    width: int
    height: int
    x: int
    y: int
    # Load the images to pygame Surfaces.
    tiles: list = []
    for name in image_files:
        tiles.append(pygame.image.load(name).convert_alpha())
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
    background = pygame.Surface((width, height))
    background.fill((167, 197, 109))
    # Blit the images to the Surface and return.
    x = 0
    y = 0
    for row in terrain_map:
        for i in row:
            background.blit(tiles[int(i)], (x, y))
            x += tile_size
        y += tile_size
        x = 0
    return background

def main() -> None:
    """Add a function description."""
    # Annotate and initialize variables
    WIDTH: int = 640
    HEIGHT: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    background_tiles: list
    sam: Student
    group: pygame.sprite.Group = pygame.sprite.Group()
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Get to class!"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background_tiles = ["tiles/grass.png",
                        "tiles/lot.png",
                        "tiles/building.png",
                        "tiles/horizontal_path.png",
                        "tiles/vertical_path.png"]
    background = make_background(background_tiles, "campus.txt")
    screen = make_window(background.get_width(), background.get_height(), caption)
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    sam = Student(pygame.image.load("class_dash_sprite.png").convert_alpha(), 25, 25)
    group.add(sam)
    #sprite = GenericSprite(pygame.image.load("genericimage.png").convert_alpha())
    #group.add(sprite)

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEMOTION:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif e.type == pygame.MOUSEBUTTONUP:
                pass
            elif e.type == pygame.KEYDOWN:
                key = e.__dict__["key"]
                if key == pygame.K_UP:
                    sam.move(Student.UP)
                elif key == pygame.K_DOWN:
                    sam.move(Student.DOWN)
                elif key == pygame.K_RIGHT:
                    sam.move(Student.RIGHT)
                elif key == pygame.K_LEFT:
                    sam.move(Student.LEFT)
            elif e.type == pygame.KEYUP:
                sam.move(Student.STOP)
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw sprites.
        group.clear(screen, background)
        group.update(screen)
        group.draw(screen)     
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
