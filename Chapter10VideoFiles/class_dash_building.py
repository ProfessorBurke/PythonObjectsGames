"""Student runs across campus."""

# Import and initialize pygame.
import pygame
pygame.init()

class Building(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

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
    _last_dx: int
    _last_dy: int
    _speed: int
    _face_right: pygame.Surface

    def __init__(self, image: pygame.Surface, x: int, y: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._face_right = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 0
        self._dy = 0
        self._last_dx = 0
        self._last_dy = 0
        self._speed = 2

    def move(self, direction: int, buildings: pygame.sprite.Group) -> None:

        if direction != Student.STOP:
            rotation: int = direction * 90
            x: int = self.rect.centerx
            y: int = self.rect.centery
            self.image = pygame.transform.rotate(self._face_right, rotation)
            self.rect.centerx = x
            self.rect.centery = y

            while pygame.sprite.spritecollide(self, buildings, False,
                                         pygame.sprite.collide_mask):
                if self._dx == 0 and self._dy == 0:
                    dx: float = -self._last_dx * 2
                    dy: float = -self._last_dy * 2
                else:
                    dx: float = -self._dx * 2
                    dy: float = -self._dy * 2
                self.rect.top += dy
                self.rect.left += dx
                
        if not (self._dx == 0  and self._dy == 0):
            self._last_dx = self._dx
            self._last_dy = self._dy

        self._dx = 0
        self._dy = 0
        if direction != Student.STOP:
            if direction == Student.LEFT:
                self._dx = -self._speed
            elif direction == Student.RIGHT:
                self._dx = self._speed
            if direction == Student.UP:
                self._dy = -self._speed
            elif direction == Student.DOWN:
                self._dy = self._speed

    def update(self, screen: pygame.Surface,
               buildings: pygame.sprite.Group) -> None:
        """Move sprite by _dx, _dy."""
        self.rect.top += self._dy
        self.rect.left += self._dx

        while pygame.sprite.spritecollide(self, buildings, False,
                                         pygame.sprite.collide_mask):
            dx: float = -self._dx * 2
            dy: float = -self._dy * 2
            self.rect.top += dy
            self.rect.left += dx
            
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width() - int(self.rect.width / 4)
        elif self.rect.left < 0:
            self.rect.left = int(self.rect.width / 4)
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
    building: Building
    building_group: pygame.sprite.Group = pygame.sprite.Group()
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
    building = Building(pygame.image.load("building.png").convert_alpha(),
                        200, 200)
    building_group.add(building)

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
                    student.move(Student.UP, building_group)
                elif key == pygame.K_DOWN:
                    student.move(Student.DOWN, building_group)
                elif key == pygame.K_RIGHT:
                    student.move(Student.RIGHT, building_group)
                elif key == pygame.K_LEFT:
                    student.move(Student.LEFT, building_group)
            # If all arrow keys are up, stop the student.
            elif e.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or
                        keys[pygame.K_RIGHT] or keys [pygame.K_LEFT]):
                    student.move(Student.STOP, building_group)

                    
        # Draw sprites.
        student_group.clear(screen, background)
        building_group.clear(screen, background)
        student_group.update(screen, building_group)
        building_group.update(screen)
        student_group.draw(screen)
        building_group.draw(screen)
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
