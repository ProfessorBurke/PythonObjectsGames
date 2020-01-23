import random
import math
from typing import ClassVar

import pygame

class StarBurst():
    """A class representing a fireworks starburst.

       Public methods: __init__, draw_burst
    """

    # Annotate and initialize class-level field
    _stars: ClassVar[list] =[
             pygame.image.load("small_red_star.png"),
             pygame.image.load("small_blue_star.png"),
             pygame.image.load("small_green_star.png"),
             pygame.image.load("small_yellow_star.png")]

    # Annotate object-level fields
    _x: float
    _y: float
    _radius: float
    _num_stars: int
    _star: pygame.Surface   
    
    def __init__(self, x: float, y: float) -> None:
        """Initialize an instance of StarBurst at x,y."""
        self._x = x
        self._y = y
        self._radius = random.randint(25, 75)
        self._num_stars = random.randint(5, 20)
        self._star = random.choice(StarBurst._stars)

    def _calc_angle(self, num_points: int) -> float:
        """Calculate and return the angle between points 
           evenly distributed around a circle."""
        DEGREES_CIRCLE: int = 360
        angle: float
    
        # Calculate and return the angle.
        angle = DEGREES_CIRCLE / num_points
        return angle
    
    def draw_burst(self, surface: pygame.Surface) -> None:
        """Draw the firework on screen."""
        # Annotate and initialize variables.
        w: int = self._star.get_width()
        h: int = self._star.get_height()
        angle_degrees: float = self._calc_angle(self._num_stars)
        angle: float = math.radians(angle_degrees)
        i: int
        x_loc: float
        y_loc: float

        # Draw the stars.
        for i in range(self._num_stars):
            x_loc = self._x + self._radius*math.cos(i*angle) - w/2
            y_loc = self._y + self._radius*math.sin(i*angle) - h/2
            surface.blit(self._star, (x_loc, y_loc))


class AnimatedBurst(StarBurst):
    """A class representing an animated fireworks starburst.

       Public methods: __init__, draw_burst
    """

    # Annotate object-level fields
    _state_index: int
    _state: list

    def __init__(self, x: int, y: int) -> None:
        """Initialize an instance of GradualBurst at x,y."""
        super().__init__(x, y)
        self._state_index = 0
        self._state = [self._radius / 5, self._radius / 4, self._radius / 3, self._radius / 2, self._radius]
        self._radius = self._state[0]

    def draw_burst(self, surface: pygame.Surface) -> None:
        """Draw the firework on surface."""
        # Change to the next radius in the list
        self._state_index = ((self._state_index + 1)
                                 % len(self._state))
        self._radius = self._state[self._state_index]
        # Draw the burst
        super().draw_burst(surface)


def make_window(size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Create and draw ten StarBursts (animated or static)."""
    # Annotate and initialize variables
    SIZE: int = 480
    user_quit: bool = False
    clock: pygame.time.Clock = pygame.time.Clock()
    screen: pygame.Surface
    background: pygame.Surface
    burst_list: list[StarBurst]
    choice: int
    x: int
    y: int
    
    # Set up assets.
    screen = make_window(SIZE, "Fireworks!")
    background = pygame.Surface((480,480))

    # Make ten starbursts.
    burst_list = []
    for i in range(10):
        choice = random.randint(0,1)
        x = random.randint(0, 480)
        y = random.randint(0, 480)
        if choice == 0:
            burst_list.append(AnimatedBurst(x, y))
        else:
            burst_list.append(StarBurst(x, y))
    
    # Run until the user closes the window.
    while not user_quit:
        # Loop five times per second
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
        screen.blit(background,(0,0))
        for burst in burst_list:
            burst.draw_burst(screen)
        pygame.display.flip()

    pygame.quit()

main()
