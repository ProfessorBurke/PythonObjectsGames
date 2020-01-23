# This file is Listing 3.1, but named so it can be imported.

import random
import math
import pygame

class StarBurst():
    """A class representing a fireworks starburst.

       Public methods: __init__, draw_burst
    """

    # Annotate object-level fields
    _x: float
    _y: float
    _radius: float
    _num_stars: int
    _star: pygame.Surface
    
    
    def __init__(self,
                 x: float,
                 y: float,
                 star: pygame.Surface) -> None:
        """Initialize an instance of StarBurst at x,y."""
        self._x = x
        self._y = y
        self._radius = random.randint(25, 75)
        self._num_stars = random.randint(5, 20)
        self._star = star

    def _calc_angle(self, num_points: int) -> float:
        """Calculate and return the angle between points 
           evenly distributed around a circle."""
        DEGREES_CIRCLE: int = 360
        angle: float
    
        # Calculate and return the angle.
        angle = DEGREES_CIRCLE / num_points
        return angle
    
    def draw_burst(self, screen: pygame.Surface) -> None:
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
            screen.blit(self._star, (x_loc, y_loc))

