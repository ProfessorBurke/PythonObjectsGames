"""Student runs across campus."""

# Import and initialize pygame.
import pygame
pygame.init()

class Background(pygame.sprite.Sprite):

    # Annotate object-level fields
    _speed: int
    _dx: int
    _dy: int

    def __init__(self, image: pygame.Surface, speed: int) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self._speed = speed
        self._dx = 0
        self._dy = 0

    def can_scroll(self, direction: int, screen: pygame.Surface) -> bool:
        result: bool = False
        if direction == Student.UP and self.rect.top < 0:
            result = True
        elif direction == Student.LEFT and self.rect.left < 0:
            result = True
        elif direction == Student.DOWN and self.rect.bottom > screen.get_height():
            result = True
        elif direction == Student.RIGHT and self.rect.right > screen.get_width():
            result = True
        return result

    def move(self, direction: int) -> None:
        self._dx = 0
        self._dy = 0
        if direction != Student.STOP:
            if direction == Student.LEFT:
                self._dx = self._speed
            elif direction == Student.RIGHT:
                self._dx = -self._speed
            if direction == Student.UP:
                self._dy = self._speed
            elif direction == Student.DOWN:
                self._dy = -self._speed

    def update(self, screen: pygame.Surface) -> None:
        """Move sprite by _dx, _dy."""
        self.rect.top += self._dy
        self.rect.left += self._dx
        if self.rect.right < screen.get_width():
            self.rect.right = screen.get_width()
        elif self.rect.left > 0:
            self.rect.left = 0
        if self.rect.bottom < screen.get_height():
            self.rect.bottom = screen.get_height()
        elif self.rect.top > 0:
            self.rect.top = 0


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

    def __init__(self, image: pygame.Surface, x: int, y: int, speed: int) -> None:
        """Initialize the sprite."""
        super().__init__()
        self._face_right = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self._dx = 0
        self._dy = 0
        self._speed = speed

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

    def update(self, screen: pygame.Surface) -> None:
        """Move sprite by _dx, _dy."""
        self.rect.top += self._dy
        self.rect.left += self._dx
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width() - int(self.rect.width / 4)
        elif self.rect.left < 0:
            self.rect.left = int(self.rect.width / 4)
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height() - int(self.rect.height / 4)
        elif self.rect.top < 0:
            self.rect.top = int(self.rect.height / 4)

    def within_threshold(self, screen: pygame.Surface, threshold: int,
                         direction: int) -> bool:
        return ((direction == Student.UP and self.rect.top < threshold)
                or (direction == Student.DOWN and self.rect.bottom >= screen.get_height() - threshold)
                or (direction == Student.LEFT and self.rect.left < threshold)
                or (direction == Student.RIGHT and self.rect.right >= screen.get_width() - threshold))
   

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
    SPEED: int = 2
    THRESHOLD: int = 20
    screen: pygame.Surface
    student: Student
    student_group: pygame.sprite.Group = pygame.sprite.Group()
    background: Background
    background_group: pygame.sprite.Group = pygame.sprite.Group()
    user_quit: bool = False
    direction: int = Student.STOP
    e: pygame.event.Event
    keys: tuple
    key: int
    caption: str = "Get to class!"

    # Set up assets.
    screen = make_window(WIDTH, HEIGHT, caption)
    clock: pygame.time.Clock = pygame.time.Clock()
    student = Student(pygame.image.load("class_dash_sprite.png").convert_alpha(),
                      25, 25, SPEED)
    student_group.add(student)
    background = Background(pygame.image.load("campus_background.png").convert_alpha(),
                            SPEED)
    background_group.add(background)

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
                    direction = Student.UP
                elif key == pygame.K_DOWN:
                    direction = Student.DOWN
                elif key == pygame.K_RIGHT:
                    direction = Student.RIGHT
                elif key == pygame.K_LEFT:
                    direction = Student.LEFT
            # If all arrow keys are up, stop the student.
            elif e.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or
                        keys[pygame.K_RIGHT] or keys [pygame.K_LEFT]):
                    direction = Student.STOP

                    
        # Draw sprites.
        if direction == Student.STOP:
            student.move(Student.STOP)
            background.move(Student.STOP)
        else:
            if student.within_threshold(screen, THRESHOLD, direction):
                if background.can_scroll(direction, screen):
                    background.move(direction)
                    student.move(Student.STOP)
                else:
                    student.move(direction)
                    background.move(Student.STOP)
            else:
                student.move(direction)
                background.move(Student.STOP)

        background_group.update(screen)
        student_group.update(screen)
        background_group.draw(screen)
        student_group.draw(screen)     
                
        # Show the display.
        pygame.display.flip()
    pygame.quit()

main()
