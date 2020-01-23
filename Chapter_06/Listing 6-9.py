"""A constellation labeling program."""
import pygame
pygame.init()

class Star():
    """A class representing a star.

       Public methods: __init__, draw, select, get_name
    """

    # Annotate object-level fields
    _x: float
    _y: float
    _name: str
    _star: pygame.Surface
    _star_selected: pygame.Surface
    _color: tuple
    
    def __init__(self, x: float, y: float, name: str, color: tuple) -> None:
        """Initialize an instance of star at x,y."""
        self._x = x
        self._y = y
        self._name = name
        self._selected = False
        self._color = color
        # self._star is a small circle in the star's color
        self._star = pygame.Surface((20,20))
        pygame.draw.circle(self._star, self._color, (10, 10), 5)
        # self._star_selected is a larger white circle
        self._star_selected = pygame.Surface((20,20))
        pygame.draw.circle(self._star_selected, (255, 255, 255), (10, 10), 10)

    def select(self, selected: bool) -> None:
        """Select or deselect according to parameter."""
        self._selected = selected

    def get_name(self) -> str:
        """Return the star's name."""
        return self._name

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the star on the surface."""
        if self._selected:
            surface.blit(self._star_selected, (self._x, self._y))
        else:
            surface.blit(self._star, (self._x, self._y))

class ConstellationIter():
    """An iterator for iterating over a Constellation's stars.

       Public methods: __init__, __iter__, __next__
    """

    # Annotate object-level variables
    _constellation: "Constellation"
    _star_index: int
    _num_stars: int
    
    def __init__(self, constellation: "Constellation", num_stars: int) -> None:
        """Initialize from parameters and set index to zero."""
        self._constellation = constellation
        self._num_stars = num_stars
        self._star_index = 0
        
    def __iter__(self) -> "ConstellationIter":
        """Return self as required by Python."""
        return self

    def __next__(self) -> Star:
        """Return the next Star in the Constellation or raise exception
           and advance the index."""
        # Annotate variable
        star: Star
        if self._star_index == self._num_stars:
            raise StopIteration
        else:
            star = self._constellation[self._star_index]
        self._star_index += 1
        return star

    def first(self) -> None:
        """Reset the iterator to the first element."""
        self._star_index = 0
         

class Constellation():
    """A class representing a constellation.

       Public methods: __init__, draw, __getitem__, __iter__
                       get_name
    """

    # Annotate object-level fields
    _stars: list
    _name: str
    
    def __init__(self, stars: list, name: str) -> None:
        """Initialize from parameters."""
        self._stars = stars
        self._name = name

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the constellation."""
        for star in self._stars:
            star.draw(surface)

    def get_name(self) -> str:
        """Return the constellation name."""
        return self._name

    def __getitem__(self, star_index: int) -> Star:
        """Allow indexing into a Constellation, return star at
           star_index."""
        return self._stars[star_index]

    def __iter__(self) -> ConstellationIter:
        """Create and return a ConstellationIter."""
        return ConstellationIter(self, len(self._stars))

def make_window(h_size: int, v_size: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen = pygame.display.set_mode((h_size, v_size))
    pygame.display.set_caption(caption)
    return screen

def read_stars(file: str, color: tuple) -> list:
    """Read and return star data from file."""
    # Annotate variables
    stars: list = []
    star: str
    star_data: list
    star_list: list
    # Open and read the file.
    with open(file) as star_file:
        star_data = star_file.readlines()
    # Split lines and organize in a 2D list.
    for star in star_data:
        star_list = star.split(",")
        stars.append(Star(int(star_list[0]),
                          int(star_list[1]),
                          star_list[2], color))
    return stars

def main() -> None:
    """Draw a constellation and allow the user to click to
       iterate through the stars."""
    # Annotate and initialize variables
    H_SIZE: int = 480
    V_SIZE: int = 480
    user_quit: bool = False
    clock: pygame.time.Clock = pygame.time.Clock()
    screen: pygame.Surface
    background: pygame.Surface
    stars: list
    orion: Constellation
    orion_iter: ConstellationIter
    selected_star: Star
    event: pygame.event.Event

    # Read in star data and create the constellation.
    stars = read_stars("orion.txt", (255, 255, 0))
    orion = Constellation(stars, "Orion")
   
    # Set up pygame assets.
    screen = make_window(H_SIZE, V_SIZE, "Orion")
    background = pygame.Surface((H_SIZE,V_SIZE))

    # Set up an iterator over the constellation.
    orion_iter = iter(orion)
    selected_star = None
    
    # Run until the user closes the window.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # Deselect current selection and select
                # next star in the Constellation
                try:
                    if selected_star != None:
                        selected_star.select(False)
                    selected_star = next(orion_iter)
                    if selected_star != None:
                        selected_star.select(True)
                        name = selected_star.get_name()
                        pygame.display.set_caption(name)
                # Reset the iterator and do it over if
                # we've reached the last star.
                except StopIteration:
                    orion_iter.first()
                    pygame.display.set_caption("Orion")
                
        screen.blit(background,(0,0))
        orion.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
