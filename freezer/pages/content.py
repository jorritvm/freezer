import reflex as rx

@rx.page(route="/content/[category]")
def content_by_category():
    """A page that updates based on the route."""
    # Displays the dynamic part of the URL, the post ID
    return rx.heading(rx.State.category)