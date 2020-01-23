"""Draw a random firework burst each time the user clicks."""
import random
import math

# Import and initialize pygame.
import pygame
pygame.init()

def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen

def get_random_star(red_star: pygame.Surface,
                    blue_star: pygame.Surface,
                    green_star: pygame.Surface,
                    yellow_star: pygame.Surface) -> pygame.Surface:
    """Randomly select a color and return a Surface
       with a star of that color."""
    # Annotate variable
    star: pygame.Surface

    # Randomly choose a color star to return.
    color: int = random.randint(1,4)
    if color == 1:
        star = red_star
    elif color == 2:
        star = blue_star
    elif color == 3:
        star = green_star
    else:
        star = yellow_star
    return star

def calc_angle(num_points: int) -> float:
    """Calculate and return the angle between points 
       evenly distributed around a circle."""
    DEGREES_CIRCLE: int = 360
    angle: float
    
    # Calculate and return the angle.
    angle = DEGREES_CIRCLE / num_points
    return angle

def draw_burst(x: int,
               y: int,
               radius: int,
               num_stars: int,
               star: pygame.Surface,
               screen: pygame.Surface) -> None:
    """Draw the firework on screen, as specified
       by parameters."""
    # Annotate variables
    angle_degrees: float
    angle: float
    offset_w: int
    offset_h: int
    i: int
    x_loc: float
    y_loc: float

    # Calculate the location of the star and blit.
    angle_degrees = calc_angle(num_stars)
    angle = math.radians(angle_degrees)
    offset_w = star.get_width() / 2
    offset_h = star.get_height() / 2
    for i in range(num_stars):
        x_loc = x + radius * math.cos(i * angle) - offset_w
        y_loc = y + radius * math.sin(i * angle) - offset_h
        screen.blit(star, (x_loc, y_loc))

def main() -> None:
    """Process clicks by drawing random bursts."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    red_star: pygame.Surface
    blue_star: pygame.Surface
    green_star: pygame.Surface
    yellow_star: pygame.Surface
    user_quit: bool = False
    event: pygame.event.Event
    x: int
    y: int
    radius: int
    num_stars: int
    star: pygame.Surface

    # Set up assets.
    screen = make_window(SIZE, "Click for a fireworks burst!")
    red_star = pygame.image.load("small_red_star.png")
    blue_star = pygame.image.load("small_blue_star.png")
    green_star = pygame.image.load("small_green_star.png")
    yellow_star = pygame.image.load("small_yellow_star.png")

    # Process events until the user chooses to quit.
    while not user_quit:
        for event in pygame.event.get():
            # Process a quit choice.
            if event.type == pygame.QUIT:
                user_quit = True
            # Process a click by drawing a starburst.
            elif event.type == pygame.MOUSEBUTTONUP:
                x = random.randint(0,SIZE)
                y = random.randint(0,SIZE)
                radius = random.randint(25, 75)
                num_stars = random.randint(5, 20)
                star = get_random_star(red_star, blue_star,
                                       green_star, yellow_star)
                draw_burst(x,y,radius,num_stars, star, screen)   
        # Show the drawing.
        pygame.display.flip()
    pygame.quit()

main()
