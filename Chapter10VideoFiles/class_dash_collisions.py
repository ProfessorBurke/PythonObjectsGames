"""Student runs across campus."""

# Imports and initialize pygame.
import random
import pygame
pygame.init()

class Pizza(pygame.sprite.Sprite):

    # Annotate object-level fields
    _energy: float

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize sprite from parameters and generate energy value."""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._energy = random.randint(1, 4) / 2

    def get_energy(self) -> float:
        """Return the energy value."""
        return self._energy

class Student(pygame.sprite.Sprite):

    # Annotate class-level constants
    UP: int = 1
    DOWN: int = 3
    LEFT: int = 2
    RIGHT: int = 0
    STOP: int = 4

    # Annotate object-level fields
    _dx: int
    _dy: int
    _speed: int
    _face_right: pygame.Surface
    _boost: float

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._face_right = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 0
        self._dy = 0
        self._speed = 2
        self._boost = 1

    def move(self, direction: int) -> None:
        self._dx = 0
        self._dy = 0
        if direction != Student.STOP:
            rotation: int = direction * 90
            x: int = self.rect.centerx
            y: int = self.rect.centery
            self.image = pygame.transform.rotate(self._face_right, rotation)
            self.rect.centerx = x
            self.rect.centery = y
            if direction == Student.LEFT:
                self._dx = -self._speed
            elif direction == Student.RIGHT:
                self._dx = self._speed
            if direction == Student.UP:
                self._dy = -self._speed
            elif direction == Student.DOWN:
                self._dy = self._speed

    def set_boost(self, boost: float) -> None:
        self._boost = boost

    def update(self, screen: pygame.Surface) -> None:
        """Move sprite by _dx, _dy."""
        self.rect.top += self._boost * self._dy
        self.rect.left += self._boost * self._dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width() - int(self.rect.width / 2)
        elif self.rect.left < 0:
            self.rect.left = int(self.rect.width / 2)
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height() - int(self.rect.height / 4)
        elif self.rect.top < 0:
            self.rect.top = int(self.rect.height / 4)
   

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Add a function description."""
    # Annotate and initialize variables
    WIDTH: int = 640
    HEIGHT: int = 480
    GRASS_COLOR: tuple = (167, 197, 109)
    screen: pygame.Surface
    background: pygame.Surface
    student: Student
    student_group: pygame.sprite.Group = pygame.sprite.Group()
    pizza_image: pygame.Surface
    pizza: Pizza
    pizza_group: pygame.sprite.Group = pygame.sprite.Group()
    collided_pizzas: list
    user_quit: bool = False
    e: pygame.event.Event
    keys: tuple
    key: int
    caption: str = "Get to class!"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(GRASS_COLOR)
    screen.blit(background, (0, 0))
    clock: pygame.time.Clock = pygame.time.Clock()
    student = Student(pygame.image.load("class_dash_sprite.png").convert_alpha(), 25, 25)
    student_group.add(student)
    pizza_image = pygame.image.load("pizza.png").convert_alpha()
    for i in range(10):
        pizza = Pizza(pizza_image,
                      random.randint(0, screen.get_width()),
                      random.randint(0, screen.get_height()))
        pizza_group.add(pizza)

    # Process events until the user chooses to quit.
    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Move the student on arrow key.
            elif e.type == pygame.KEYDOWN:
                key = e.__dict__["key"]
                if key == pygame.K_UP:
                    student.move(Student.UP)
                elif key == pygame.K_DOWN:
                    student.move(Student.DOWN)
                elif key == pygame.K_RIGHT:
                    student.move(Student.RIGHT)
                elif key == pygame.K_LEFT:
                    student.move(Student.LEFT)
            # If all arrow keys are up, stop the student.
            elif e.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or
                        keys[pygame.K_RIGHT] or keys [pygame.K_LEFT]):
                    student.move(Student.STOP)

        collided_pizzas = pygame.sprite.spritecollide(student,
                                                      pizza_group,
                                                      True)
        for pizza in collided_pizzas:
            energy: float = pizza.get_energy()
            print(energy)
            student.set_boost(energy)
         
        # Draw sprites.
        pizza_group.clear(screen, background)
        student_group.clear(screen, background)
        pizza_group.update(screen)
        student_group.update(screen)
        pizza_group.draw(screen)
        student_group.draw(screen)     
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
