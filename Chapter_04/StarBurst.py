# Listing 4.3, named so we can import it

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

