"""Tiling background demo."""

# Import and initialize pygame.
import pygame
pygame.init()

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
    background = pygame.Surface((width, height)) 
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
    """The arrow keys move the penguin or scroll."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    LEFT: int = 0
    RIGHT: int = 1
    NOT_MOVING: int = -1
    screen: pygame.Surface
    background: pygame.Surface
    penguin_left: pygame.Surface
    penguin_right: pygame.Surface
    penguin: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    penguin_x: int = 0
    penguin_y: int = SCREEN_SIZE - 138
    background_x: int = 0
    background_y: int = 0
    move_amount: int = 5
    scroll_threshold: int = 100
    moving: int = NOT_MOVING
    
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Scrolling Background")
    image_files: list = ["ice_block.jpg","ice.jpg","ice_top.jpg","ice_wall.jpg","ice_bottom.jpg"]
    background = make_background(image_files, "ice_castle.txt")
    penguin_right = pygame.image.load("penguin.png")
    penguin_right = penguin_right.convert_alpha()
    penguin_left = pygame.transform.flip(penguin_right, True, False)
    penguin = penguin_right
    clock: pygame.time.Clock = pygame.time.Clock()

    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_LEFT:
                    moving = LEFT
                    penguin = penguin_left
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    moving = RIGHT
                    penguin = penguin_right
            elif e.type == pygame.KEYUP:
                moving = NOT_MOVING
 
        # Move the penguin or the background
        if moving == LEFT:
            if penguin_x < scroll_threshold and background_x < 0:
                background_x += move_amount
                if background_x > 0:
                    background_x = 0
            else:
                penguin_x -= move_amount
                if penguin_x < 0:
                    penguin_x = 0
        elif moving == RIGHT:
            if (penguin_x + penguin.get_width() > screen.get_width() - scroll_threshold
                   and background_x + background.get_width() > screen.get_width()):
                background_x -= move_amount
                if background_x + background.get_width() < screen.get_width():
                    background_x = -(background.get_width()-screen.get_width())
            else:
                penguin_x += move_amount
                if penguin_x > screen.get_width() - penguin.get_width():
                    penguin_x = screen.get_width() - penguin.get_width()

        # Draw to the screen and show.
        screen.blit(background, (background_x, background_y))
        screen.blit(penguin, (penguin_x, penguin_y))
        pygame.display.flip()
         
    pygame.quit()

main()
