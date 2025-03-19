import reflex as rx
from ..state import State
from ..models import FreezerContent

@rx.page(route="/content/[category]", on_load=State.list_contents())
def content_by_category() -> rx.Component:
    """A page that updates based on the route."""
    # Displays the dynamic part of the URL, the post ID
    return rx.vstack(
        home_and_filter_buttons(),
        rx.foreach(State.contents, articly_entry),
        gap="0px"
    )
    # return

def home_and_filter_buttons() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Home",
            on_click=lambda: rx.redirect("/"),
            color_scheme="blue",
            height="100%",
            font_size="2em",
            width="50%",
            padding = "10px"
        ),
        rx.button(
            "Filter",
            on_click=lambda: rx.redirect("/category_filter"),
            color_scheme="green",
            height="100%",
            font_size="2em",
            width="50%",
            padding = "10px"
        ),
        width = "100%",
    )

def articly_entry(freezer_article: FreezerContent) -> rx.Component:
    # make the state filter the FreezerContent by this category parameter
    State.list_contents()

    return rx.grid(
        rx.text(freezer_article.category),
        rx.text(freezer_article.article),
        rx.text(freezer_article.expiration_date),
        rx.icon("pencil", width="30px"),
        rx.icon("circle-x", width="30px"),
        columns="1fr 3fr 2fr 30px 30px", # columns="5",
        gap="10px",  # Add spacing between elements
        padding="10px",  # Add padding inside the border
        border="1px solid black",  # Add a border around each entry
        width="100%",  # Ensure the entry covers the full width
    )