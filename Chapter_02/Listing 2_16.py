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
    """Process clicks by drawing bursts at click location."""
    # Annotate and initialize variables
    SIZE: int = 480
    screen: pygame.Surface
    stars: list
    user_quit: bool = False
    event: pygame.event.Event
    x: int
    y: int
    radius: int
    num_stars: int
    star: pygame.Surface

    # Set up assets.
    screen = make_window(SIZE, "Click for a fireworks burst!")
    stars = [pygame.image.load("small_red_star.png"),
             pygame.image.load("small_blue_star.png"),
             pygame.image.load("small_green_star.png"),
             pygame.image.load("small_yellow_star.png")] 

    # Process events until the user chooses to quit.
    while not user_quit:
        for event in pygame.event.get():
            # Process a quit choice.
            if event.type == pygame.QUIT:
                user_quit = True
            # Process a click by drawing a starburst.
            elif event.type == pygame.MOUSEBUTTONUP:
                x = event.__dict__["pos"][0]
                y = event.__dict__["pos"][1]
                radius = random.randint(25, 75)
                num_stars = random.randint(5, 20)
                star = random.choice(stars)
                draw_burst(x,y,radius,num_stars, star, screen)   
        # Show the drawing.
        pygame.display.flip()
    pygame.quit()

main()
