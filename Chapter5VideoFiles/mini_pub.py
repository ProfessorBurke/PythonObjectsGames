import webbrowser

class ContentItem():
    """A class representing a content item for a publication.

       Public methods: __init__, str
    """

    # Annotate object-level field
    _content: str
    
    def __init__(self, content: str) -> None:
        """Initialize from parameter."""
        self._content = content

    def __str__(self) -> str:
        return self._content


class Ad(ContentItem):
    """A class representing an advertisement for a publication.

       Public methods: __init__
    """
    # Annotate object-level field
    _url: str

    def __init__(self, content: str, url: str) -> None:
        """Initialize from parameters."""
        super().__init__(content)
        self._url = url


class Page():
    """A class representing a page of a web publication.

       Public methods:  __init__, add_item
    """

    # Annotate object-level fields
    _content_items: "list[ContentItem]" 

    def __init__(self):
        """Set content to empty."""
        self._content_items = []

    def add_item(self, item: ContentItem) -> None:
        """Add the item to the content list."""
        self._content_items.append(item)

    def show(self) -> None:
        """Show the content."""
        for item in self._content_items:
            print(item)

def main():
    # Create the publication content
    content = ContentItem("Lorem ipsum dolor sit amet.")
    ad = Ad("Visit Niagara!", "https://niagarafalls.ca/")
    page = Page()
    page.add_item(content)
    page.add_item(ad)
    page.show()

main()
            
