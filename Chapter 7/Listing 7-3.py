"""A projectile motion program demonstrating an observer
   pattern with multiple inheritance."""
import math
import pygame
pygame.init()
class Observer():
    """An observer mixin for the observer pattern.

       Public methods:  __init__, update
    """
    # Annotate object-level fields
    executor: object

    def __init__(self, executor: object, **kwargs) -> None:
        """Initialize field from parameter."""
        super().__init__(**kwargs)
        self.executor = executor
        self.executor.attach(self)

    def update() -> None:
        pass

class Projectile():
    """A projectile motion calculator.

       Public methods: __init__, handle_key, notify,
                      attach, detach, get_updated_data
    """
    # Annotate and initialize class-level constants
    NONE: int = 0
    ANGLE: int = 1
    VELOCITY: int = 2
    RADIANS_MOD: float = math.pi / 180
    VELOCITY_MOD: float = 1.0

    # Annotate object-level fields
    _angle_radians: float
    _velocity: float
    _mode: int
    _observers: list

    def __init__(self, angle: float, velocity: float) -> None:
        """Initialize fields from parameters, init mode and observers."""
        self._angle_radians = angle
        self._velocity = velocity
        self._mode = Projectile.NONE
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """Attach the observer parameter."""
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach the observer parameter."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers of a change in state."""
        for observer in self._observers:
            observer.update()

    def get_angle(self) -> float:
        """Return the angle."""
        return self._angle_radians

    def get_velocity(self) -> float:
        """Return the velocity."""
        return self._velocity

    def get_flight_time(self) -> float:
        """Return the time of flight."""
        return math.ceil(2 * math.sin(self._angle_radians) * self._velocity / 9.8)

    def get_max_height(self) -> float:
        """Return the maximum height."""
        return self._velocity**2 * (math.sin(self._angle_radians))**2 / (2 * 9.8)

    def get_horizontal_range(self) -> float:
        """Return the distance traveled."""
        return self._velocity**2 * math.sin(2 * self._angle_radians) / 9.8

    def handle_key(self, key: int) -> None:
        """Handle a keypress."""
        # Change the mode.
        if key == pygame.K_a:
            self._mode = Projectile.ANGLE
        elif key == pygame.K_v:
            self._mode = Projectile.VELOCITY
        # Change a value.
        elif key == pygame.K_UP:
            if self._mode == Projectile.ANGLE:
                self._angle_radians += Projectile.RADIANS_MOD
                self.notify()
            elif self._mode == Projectile.VELOCITY:
                self._velocity += Projectile.VELOCITY_MOD
                self.notify()
        elif key == pygame.K_DOWN:
            if self._mode == Projectile.ANGLE:
                self._angle_radians -= Projectile.RADIANS_MOD
                self.notify()
            elif self._mode == Projectile.VELOCITY:
                self._velocity -= Projectile.VELOCITY_MOD
                self.notify()

class TextView():
    """Displays text information on the screen.

       Public methods:  __init__, draw
    """
    # Annotate object-level fields
    _x: float
    _y: float
    _text: str
    
    def __init__(self, x: float, y: float, **kwargs) -> None:
        """Initialize fields from parameters."""
        super().__init__(**kwargs)
        self._x = x
        self._y = y
        self._text = ""

    def set_text(self, text: str) -> None:
        """Set the label text."""
        self._text = text

    def draw(self, surface: pygame.Surface) -> None:
        """Draw to surface."""
        # Annotate variables
        font: pygame.font.Font
        label_surface: pygame.Surface
        
        font = pygame.font.SysFont("Helvetica", 30)
        label_surface = font.render(self._text,
                                    True, (255, 255, 255))
        surface.blit(label_surface, (self._x, self._y))    

class TextViewObserver(TextView, Observer):
    """A TextView that is synchronized with an object.

       Public methods:  __init__, update
    """

    def __init__(self, **kwargs) -> None:
        """Initialize superclass parts of the object and update."""
        super().__init__(**kwargs)
        radians: float = self.executor.get_angle()
        velocity: float = self.executor.get_velocity()
        self.set_text("{:.1f} degrees, {:.1f} m/s".format(math.degrees(radians), velocity))

    def update(self) -> None:
        """Update the textview based on new data."""
        radians: float = self.executor.get_angle()
        velocity: float = self.executor.get_velocity()
        self.set_text("{:.1f} degrees, {:.1f} m/s".format(math.degrees(radians), velocity)) 
              
class ProjectilePlot():
    """A plot of a projectile motion equation.

       Public methods:  __init__, draw
    """
    # Annotate object-level fields
    _x: float
    _y: float
    _plot: pygame.Surface
    
    def __init__(self, x: float, y: float, **kwargs) -> None:
        """Initialize fields from parameters."""
        super().__init__(**kwargs)
        self._x = x
        self._y = y
        self._plot = pygame.Surface((300, 300))

    def update_plot(self, v_zero: float, theta: float) -> None:
        """Update the plot to reflect new values."""
        # Clear the drawing.
        self._plot.fill((255, 255, 255))
        # Draw a grid.
        for x in range(10, 301, 10):
            pygame.draw.line(self._plot, (200, 200, 200), (x, 0), (x, 290))
        for y in range(10, 301, 10):
            pygame.draw.line(self._plot, (200, 200, 200), (10, y), (300, y))            
        # Plot the projectile.
        time: float = math.ceil(2 * math.sin(theta) * v_zero / 9.8)
        for t in range(time + 1):
            x = v_zero * math.cos(theta) * t
            y = v_zero * math.sin(theta) * t - (.5 * 9.8 * t**2)
            pygame.draw.circle(self._plot, (0, 0, 0), (int(10 + x), int(290-y)), 3)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the plot."""
        surface.blit(self._plot, (self._x, self._y))

class PlotObserver(ProjectilePlot, Observer):
    """A plot that is synchronized with an object.

       Public methods:  __init__, update
    """
    def __init__(self, **kwargs) -> None:
        """Initialize superclass parts of the object and update."""
        super().__init__(**kwargs)
        self.update_plot(self.executor.get_velocity(), self.executor.get_angle())

    def update(self) -> None:
        """Update the plot based on new data."""
        self.update_plot(self.executor.get_velocity(), self.executor.get_angle())

def main():
    """Run the main event loop."""
    # Annotate variables.
    projectile: Projectile
    event: pygame.event.Event
    text_view: TextViewObserver
    plot: PlotObserver
    screen: pygame.Surface
    background: pygame.Surface
    key: int
    user_quit: bool = False
    clock: pygame.time.Clock = pygame.time.Clock()

    # Initialize pygame and enable events for pressed keys.
    pygame.init()
    pygame.key.set_repeat(1, 100)
    
    # Create assets.
    projectile = Projectile(math.pi / 6, 100)
    text_view = TextViewObserver(executor = projectile,
                                 x = 15, y = 15)
    plot = PlotObserver(executor = projectile, x = 90, y = 100)

    # Create a window.
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Projectile motion")
    background = pygame.Surface((480, 480))
    background.fill((90, 110, 130))

    # Run until the user closes the window.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
            elif event.type == pygame.KEYDOWN:
                # Send key events to the Projectile
                key = event.__dict__["key"]
                projectile.handle_key(key)
                    
        # Draw the background and picture               
        screen.blit(background,(0,0))
        text_view.draw(screen)
        plot.draw(screen)
        pygame.display.flip()

main()
pygame.quit()


    
