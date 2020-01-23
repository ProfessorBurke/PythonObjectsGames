"""A constellation labeling program."""
from typing import ClassVar
import pygame

class Star():
    """A class representing a star.

       Public methods: __init__, draw, select, get_name, set_color
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
        """Select or deselected according to parameter."""
        self._selected = selected

    def set_color(self, color: tuple) -> None:
        """Set the star's color to the parameter."""
        self._color = color
        pygame.draw.circle(self._star, self._color, (10, 10), 5)

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

       Public methods: __init__, __iter__, __next__, first
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
                       get_name, update
    """

    # Annotate object-level fields
    _stars: list
    _name: str
    _button_manager: "ButtonGroup"
    
    def __init__(self, stars: list, name: str, button_manager: "ButtonGroup") -> None:
        """Initialize from parameters."""
        self._stars = stars
        self._name = name
        self._button_manager = button_manager
        button_manager.attach(self)

    def update(self) -> None:
        """Update stars to reflect selected button."""
        star_color = self._button_manager.get_selected_color()
        for star in self._stars:
            star.set_color(star_color)

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

class Button():
    """A button that can be moused over and pressed.

       Public methods: __init__, set_state, get_color, 
                       draw, point_in
    """

    # Annotate and define class-level fields
    MOUSE_OUT: ClassVar[int] = 0
    MOUSE_OVER: ClassVar[int] = 1
    SELECTED: ClassVar[int] = 2

    # Annotate object-level fields
    _text: str
    _state: int
    _color: tuple 
    _rect: pygame.Rect 
    _text_surface: pygame.Surface

    def __init__(self, text: str, color: tuple,
                 rect: pygame.Rect, state: int) -> None:
        """Initialize from parameters and make text Surface."""
        self._text = text
        self._state = state
        self._color = color
        self._rect = rect
        font = pygame.font.SysFont("Verdana", 18)
        self._text_surface = font.render(self._text, 1, (25, 25, 25))

    def set_state(self, state: int) -> None:
        """Change the button's state to parameter."""
        self._state = state

    def get_color(self) -> tuple:
        """Return the button's color."""
        return self._color
        
    def draw(self, surface: pygame.Surface) -> None:
        """Draw to Surface."""
        # Create the surfaces and fill the background.
        button = pygame.Surface((100, 50))
        button.fill((255, 255, 255))
        raised = pygame.Surface((100, 50))
        shadow = pygame.Surface((100, 50))

        if self._state == Button.MOUSE_OUT:
            # Draw a light gray button with shadow.
            raised.fill((245, 245, 245))
            shadow.fill((225, 225, 225))
            button.blit(shadow, (2, 2))
            button.blit(raised, (-2, -2))
        elif self._state == Button.MOUSE_OVER:
            # Draw a button in light color with shadow.
            r = (self._color[0]+150 if self._color[0] < 155
                 else self._color[0])
            g = self._color[1]+150 if self._color[1] < 155 else self._color[1]
            b = self._color[2]+150 if self._color[2] < 155 else self._color[2]
            raised.fill((r, g, b))
            shadow.fill((225, 225, 225))
            button.blit(shadow, (-2, -2))
            button.blit(raised, (2, 2))            
        else:
            # (SELECTED) Draw a button in color with shadow.
            raised.fill(self._color)
            shadow.fill((225, 225, 225))
            button.blit(shadow, (-2, -2))
            button.blit(raised, (2, 2))
        # Blit the text and then the button to surface.
        button.blit(self._text_surface, (15, 15))
        surface.blit(button, (self._rect.left, self._rect.top))

    def point_in(self, point: tuple) -> bool:
        """Return True if point within rect."""
        return (self._rect.left <= point[0] and self._rect.right >= point[0]
                and self._rect.top <= point[1] and self._rect.bottom >= point[1])

class ButtonGroup():
    """A class to manage a group of related buttons.
       This is a subject in an observer pattern.

       Public methods: __init__, attach, detach, notify,
                       get_selected_color, point_in,
                       handle_click, handle_mouse_over, draw
    """

    # Annotate object-level variables    
    _buttons: list
    _selected: Button
    _rect: pygame.Rect
    _observers: list
    
    def __init__(self, rect: pygame.Rect) -> None:
        """Initialize from parameter and create buttons and observer list."""
        self._rect = rect
        self._buttons = []
        self._buttons.append(Button("Red", (255, 0, 0), pygame.Rect(20, 495, 100, 50), Button.MOUSE_OUT))
        self._buttons.append(Button("Blue", (0, 0, 255), pygame.Rect(130, 495, 100, 50), Button.MOUSE_OUT))
        self._buttons.append(Button("White", (255, 255, 255), pygame.Rect(240, 495, 100, 50), Button.MOUSE_OUT))
        self._buttons.append(Button("Yellow", (255, 255, 0),pygame.Rect(350, 495, 100, 50), Button.SELECTED))
        self._selected = self._buttons[3]
        self._observers = []

    def attach(self, observer: object) -> None:
        """Allow an observer to attach."""
        self._observers.append(observer)

    def detach(self, observer: object) -> None:
        """Allow an observer to detach."""
        if observer in self._observers:
            observer.remove()

    def notify(self) -> None:
        """Notify observers of a state change."""
        for observer in self._observers:
            observer.update()

    def get_selected_color(self) -> tuple:
        """Return the color of the selected button."""
        return self._selected.get_color()
        
    def point_in(self, point: tuple) -> bool:
        """Return True if point within rect."""
        return (self._rect.left <= point[0] and self._rect.right >= point[0]
                and self._rect.top <= point[1] and self._rect.bottom >= point[1])

    def handle_click(self, point: tuple) -> None:
        """Handle the click by changing button selection if appropriate."""
        # Annotate variables
        new_selection: Button = None
        i = 0
        while i < len(self._buttons) and new_selection == None:
            if not self._selected == self._buttons[i]:
                if self._buttons[i].point_in(point):
                    new_selection = self._buttons[i]
                    new_selection.set_state(Button.SELECTED)
                    self._selected.set_state(Button.MOUSE_OUT)
                    self._selected = new_selection
                    self.notify()
            i += 1
    
    def handle_mouse_over(self, point: tuple) -> None:
        """Handle the mouseover by highlighting button, if appropriate."""
        for button in self._buttons:
            if not self._selected == button:
                button.set_state(Button.MOUSE_OUT)
                if button.point_in(point):
                    button.set_state(Button.MOUSE_OVER)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw a white background and all buttons."""
        background = pygame.Surface((480, 80))
        background.fill((255, 255, 255))
        surface.blit(background, (0, 480))
        for button in self._buttons:
            button.draw(surface)
        
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
                          star_list[2],
                          color))
    return stars

def main() -> None:
    """Draw a constellation and allow the user to click to
       iterate through the stars and set star color."""
    # Annotate and initialize variables
    H_SIZE: int = 480
    V_SIZE: int = 560
    user_quit: bool = False
    clock: pygame.time.Clock = pygame.time.Clock()
    screen: pygame.Surface
    background: pygame.Surface
    stars: list
    orion: Constellation
    orion_iter: ConstellationIter
    selected_star: Star
    event: pygame.event.Event
    button_group: ButtonGroup

    # Initialize pygame
    pygame.init()
   
    # Set up assets.
    screen = make_window(H_SIZE, V_SIZE, "Orion")
    background = pygame.Surface((H_SIZE,V_SIZE))
    button_group = ButtonGroup(pygame.Rect(0, H_SIZE, H_SIZE, V_SIZE-H_SIZE))

    # Read in star data and create the constellation.
    stars = read_stars("orion.txt", (255, 255, 0))
    orion = Constellation(stars, "Orion", button_group)

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
            elif event.type == pygame.MOUSEMOTION:
                button_group.handle_mouse_over(event.__dict__["pos"])
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check if it's a button click
                if button_group.point_in(event.__dict__["pos"]):
                    button_group.handle_click(event.__dict__["pos"])
                # Otherwise it's within the constellation pane
                else:
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
                    # Create a new iterator and do it over if
                    # we've reached the last star.
                    except StopIteration:
                        orion_iter.first()
                        pygame.display.set_caption("Orion")
                
        screen.blit(background,(0,0))
        orion.draw(screen)
        button_group.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
