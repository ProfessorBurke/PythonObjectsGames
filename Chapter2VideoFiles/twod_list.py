"""Store clicks for image locations."""

import pygame

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
    coordinates: list = []
    i: int

    # Create a pygame window.
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Click to specify the location for an image")

    # Create a background.
    background = pygame.Surface((SIZE, SIZE))
    background.fill((168, 210, 210))

    # Load in the image.
    image = pygame.image.load("van_gogh.png")
    
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
                coordinates.append([click_x, click_y])

        screen.blit(background, (0, 0))
        i = 0
        while i < len(coordinates):
            coordinates[i][0] += .1
            coordinates[i][1] += .1
            screen.blit(image, (coordinates[i][0], coordinates[i][1]))
            i += 1
        pygame.display.flip()

    pygame.quit()

main()
