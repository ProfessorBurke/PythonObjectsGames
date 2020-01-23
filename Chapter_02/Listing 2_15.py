"""Draw a random firework burst each time the user clicks."""
import random
import math

# Import and initialize pygame.
import pygame
pygame.init()

# Define constants.
SIZE: int = 480
X_COORD: int = 0
Y_COORD: int = 1
RADIUS: int = 2
NUM_STARS: int = 3
STAR: int = 4

def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen

def calc_angle(num_points: int) -> float:
    """Calculate and return the angle between points 
       evenly distributed around a circle."""
    DEGREES_CIRCLE: int = 360
    angle: int
    
    # Calculate and return the angle.
    angle = DEGREES_CIRCLE / num_points
    return angle

def draw_burst(burst: list, screen: pygame.Surface) -> None:
    """Draw the firework on screen, as specified
       by burst parameter."""
    # Annotate variables
    angle_degrees: float
    angle: float
    x_loc: float
    y_loc: float
    i: int
    
    angle_degrees = calc_angle(burst[NUM_STARS])
    angle = math.radians(angle_degrees)
    for i in range(burst[NUM_STARS]):
        x_loc = burst[X_COORD] + burst[RADIUS] * math.cos(i * angle)
        y_loc = burst[Y_COORD] + burst[RADIUS] * math.sin(i * angle)
        screen.blit(burst[STAR], (x_loc, y_loc))
        
def create_bursts(stars: list) -> list:
    """Create and return a 2d list of starburst information."""
    # Annotate and initialize variables
    bursts: list = []
    i: int
    x: int
    y: int
    radius: int
    num_stars: int
    star: pygame.Surface

    for i in range(10):
        x = random.randint(0,SIZE)
        y = random.randint(0,SIZE)
        radius = random.randint(25, 75)
        num_stars = random.randint(5, 20)
        star = random.choice(stars)
        new_burst = [x, y, radius, num_stars, star]
        bursts.append(new_burst)  
    return bursts

def draw_bursts(screen: pygame.Surface, bursts: list) -> None:
    """Draw the starbursts defined in the list bursts."""
    burst: list
    for burst in bursts:
        draw_burst(burst, screen) 

def main() -> None:
    """Store burst information in a two-dimensional list and draw."""
    # Annotate variables
    screen: pygame.Surface
    stars: list
    bursts: list
    user_quit: bool
    event: pygame.event.Event
    
    # Set up assets.
    screen = make_window(SIZE, "Fireworks!")
    stars = [pygame.image.load("small_red_star.png"),
             pygame.image.load("small_blue_star.png"),
             pygame.image.load("small_green_star.png"),
             pygame.image.load("small_yellow_star.png")] 

    # Create the list of starburst data and draw.
    bursts = create_bursts(stars)
    draw_bursts(screen, bursts)
    pygame.display.flip()

    # Wait for the user to close the window.
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
    pygame.quit()

main()
