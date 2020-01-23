"""Font demonstration."""

# Import and initialize pygame.
import pygame
pygame.init()


def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

def main() -> None:
    """Create and render fonts."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 250
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    sys_font: pygame.font.Font
    file_font: pygame.font.Font
    font_surf: pygame.Surface
    
    # Set up the window.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Fonts")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Make, render, and display the fonts.
    sys_font = pygame.font.SysFont("cambria", 36)
    file_font = pygame.font.Font("game-asset.ttf", 36)
    font_surf = sys_font.render("Hello, world!", True, (0, 0, 0))
    screen.blit(font_surf, (10, 10))
    font_surf = file_font.render("HELLO WORLD", True, (0, 255, 0))
    screen.blit(font_surf, (10, 60))

    # Make some changes, render, and display more.
    sys_font.set_bold(True)
    sys_font.set_italic(True)
    sys_font.set_underline(True)
    font_surf = sys_font.render("Hello, again!", True, (255, 0, 0))
    screen.blit(font_surf, (10, 100))
    pygame.display.flip()

    print(sys_font.size("Hello, world!"))

    while not user_quit:
        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
                         
    pygame.quit()

main()
