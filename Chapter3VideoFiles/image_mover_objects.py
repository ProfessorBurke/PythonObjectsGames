"""Allow the user to move images in a window."""

import pygame
from Image import *

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
    images: list
    selection: Image = None

    # Create a pygame window.
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Click on an image and then click to move it")

    # Load the image in.
    images = [Image("van_gogh.png", 0, 0), Image("kahlo.png", 0, 0), Image("escher.png", 0, 0)]

    # Create a background.
    background = pygame.Surface((SIZE, SIZE))
    background.fill((168, 210, 210))

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
                    selection.set_center(click_x, click_y)
                    selection.deselect()
                    selection = None
                else:
                    for image in images:
                        if image.contained_in(click_x, click_y):
                            selection = image
                    if selection:
                        selection.select()

        screen.blit(background, (0, 0))
        for image in images:
            image.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
