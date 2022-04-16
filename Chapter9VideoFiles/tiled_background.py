"""Draw a tiled background."""

# Import and initialize pygame.
import pygame
pygame.init()

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Add a function description."""
    # Annotate and initialize variables
    width: int
    height: int
    tile_width: int
    tile_height: int
    tiles: list
    i: int
    terrain: list = []
    x: int = 0
    y: int = 0
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    caption: str = "Add a window caption here"

    # Set up assets.
    # Load the terrain text file.
    with open("terrain.txt") as terrain_file:
        line = terrain_file.readline()
        while line != "":
            terrain.append(line.split())
            line = terrain_file.readline()
    # Load the tile Surfaces.
    tiles =[pygame.image.load("tiles/0_tile.jpg"),
        pygame.image.load("tiles/1_tile.jpg"),
        pygame.image.load("tiles/2_tile.jpg"),
        pygame.image.load("tiles/3_tile.jpg"),
        pygame.image.load("tiles/4_tile.jpg")]
    # Calculate the size of the Surface and create.
    tile_width = tiles[0].get_width()
    tile_height = tiles[0].get_height()
    width = len(terrain[0]) * tile_width
    height = len(terrain) * tile_height
    # Create the screen and background
    screen = make_window(width, height, caption)
    background = pygame.Surface((width, height))
    # Build the background from the terrain
    for row in terrain:
        for i in row:
            background.blit(tiles[int(i)],(x, y))
            x += tile_width
        y += tile_height
        x = 0
    # Convert the tiles.
    for i in range(len(tiles)):
        tiles[i] = tiles[i].convert()

    # Create the clock for timing the game loop.
    clock: pygame.time.Clock = pygame.time.Clock()

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
                pass
            elif e.type == pygame.KEYUP:
                pass
            elif e.type == pygame.ACTIVEEVENT:
                pass
                    
        # Draw the background.
        screen.blit(background, (0, 0))
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
