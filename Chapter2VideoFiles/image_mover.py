"""Allow the user to move images in a window."""

import pygame

def load_image(file_name: str) -> pygame.Surface:
    """Load image from file_name and return as Surface."""
    image: pygame.Surface
    image = pygame.image.load(file_name)
    image.convert()
    return image

def move(x: int, y: int, image: pygame.Surface) -> tuple:
    """Move the center of image to (x,y) and return the image's
       new (left, top) coordinate."""
    left: int
    top: int
    left = x - image.get_width() // 2
    top = y - image.get_height() // 2
    return (left, top)

def select(x: int, y: int, image_x: int, image_y: int, image: pygame.Surface) -> pygame.Surface:
    """Return the image in which (x,y) falls, or None."""
    selection: pygame.Surface = None
    if (image_x <= x and x <= image_x + image.get_width()
        and image_y <= y and y <= image_y + image.get_height()):
        selection = image
    return selection

def main() -> None:
    """The main event loop.  Handle clicks until the user quits."""
    # Define constants and annotate variables
    SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool
    event: pygame.event.Event
    click_x: int
    click_y: int
    image: pygame.Surface
    image_x: int = 0
    image_y: int = 0
    selection: pygame.Surface = None

    # Create a pygame window.
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Click on an image and then click to move it")

    # Create a background.
    background = pygame.Surface((SIZE, SIZE))
    background.fill((168, 210, 210))

    # Load in the image.
    image = load_image("van_gogh.png")
    
    # Wait for the user to quit.
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            # Process a quit choice.
            if event.type == pygame.QUIT:
                user_quit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                click_x = event.__dict__["pos"][0]
                click_y = event.__dict__["pos"][1]
                if selection:
                    (image_x, image_y) = move(click_x, click_y, selection)
                    selection = None
                else:
                    selection = select(click_x, click_y, image_x, image_y, image)

        screen.blit(background, (0, 0))
        screen.blit(image, (image_x, image_y))
        pygame.display.flip()

    pygame.quit()

main()
