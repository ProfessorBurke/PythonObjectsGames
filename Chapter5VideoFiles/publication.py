import webbrowser
import pygame

class ContentItem():
    """A class representing a content item for a publication.

       Public methods: __init__, set_x, set_y, get_height, get_width, draw,
                       clicked_in, handle_click
    """

    # Annotate object-level fields
    _image: pygame.Surface
    _x: int
    _y: int

    def __init__(self, image: pygame.Surface) -> None:
        """Initialize a ContentItem from parameters and set x,y to 0,0."""
        self._image = image
        self._x = 0
        self._y = 0

    def set_x(self, x: int) -> None:
        """Set the x value to the parameter."""
        self._x = x

    def set_y(self, y: int) -> None:
        """Set the y value to the parameter."""
        self._y = y

    def get_height(self) -> int:
        """Return the height of the ContentItem."""
        return self._image.get_height()

    def get_width(self) -> int:
        """Return the width of the ContentItem."""
        return self._image.get_width()

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the ContentItem to the Surface passed."""
        surface.blit(self._image, (self._x, self._y))

    def clicked_in(self, click_x: int, click_y: int) -> bool:
        """Return True if the x,y parameter is within the ContentItem."""
        bottom = self._y + self._image.get_height()
        right = self._x + self._image.get_width()
        return (self._y <= click_y and bottom >= click_y
                and self._x <= click_x and right >= click_x)

    def handle_click(self, click_x: int, click_y: int) -> None:
        """Handle a click within the ContentItem by doing nothing."""
        pass

class Ad(ContentItem):
    """Represent an Ad ContentItem.

       Public methods: __init__, handle_click
    """
    # Annotate object-level fields
    _url: str

    def __init__(self, image: pygame.Surface, url: str) -> None:
        """Initialize an Ad from parameters."""
        super().__init__(image)
        self._url = url
        
    def handle_click(self, click_x: int, click_y: int) -> None:
        """Handle a click within the Ad by opening the URL."""
        webbrowser.open(self._url)
        
class Page():
    """A class representing a page of a web publication.

       Public methods:  __init__, add_item, draw, handle_click
    """
    # Annotate object-level fields
    _content: "list[ContentItem]"

    def __init__(self):
        """Set content to empty."""
        self._content = []

    def add_item(self, item: ContentItem) -> None:
        """Add the parameter ContentItem to the content list."""
        self._content.append(item)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw all content."""
        # Annotate and initialize variables
        OFFSET: int = 10
        y: int = 10
        x: int = 10
        content_item: ContentItem

        # Set coordinates and draw.
        for content_item in self._content:
            content_item.set_y(y)
            content_item.set_x(x)
            y += content_item.get_height() + OFFSET
            content_item.draw(surface)

    def handle_click(self, click_x: int, click_y: int) -> None:
        """Find item that was clicked in (if any) and have it handle click."""
        # Annotate variable
        content_item: ContentItem
        
        for content_item in self._content:
            if content_item.clicked_in(click_x, click_y):
                content_item.handle_click(click_x, click_y)

                
def main():
    """Create a Page with some content and handle clicks until quit."""
    # Annotate variables
    screen: pygame.Surface
    lorem: pygame.image
    niagara: pygame.image
    content: ContentItem
    ad: Ad
    page: Page
    event: pygame.event.Event
    user_quit: bool
    
    # Create a pygame window.
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Publication Example")

    # Create the publication content.
    lorem = pygame.image.load("lorem.jpg")
    niagara = pygame.image.load("niagara ad.jpg")
    content = ContentItem(lorem)
    ad = Ad(niagara, "https://niagarafalls.ca/")
    page = Page()
    page.add_item(content)
    page.add_item(ad)

    # Draw the page.
    page.draw(screen)
    pygame.display.flip()
    
    # Wait for the user to close the window.
    user_quit = False
    while not user_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_quit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                page.handle_click(event.pos[0], event.pos[1])
    pygame.quit()



main()
            
