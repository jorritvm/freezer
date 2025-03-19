import reflex as rx
from ..state import State

@rx.page(route="/category_filter", on_load=State.list_categories())
def category_filter() -> rx.Component:
    # dynamically generate me category filter buttons in 2 columns

    def category_button(category):
        return rx.button(
            category,
            height="100%",  # Make the button take the full height of the grid cell
            font_size="2em",
            on_click=lambda: rx.redirect("/content/" + category + "/" + State.memoize_sort_by),
        )

    all_button = rx.button(
        "geen filter",
        color_scheme="green",
        height="100%",  # Make the button take the full height of the grid cell
        font_size="2em",
        on_click=lambda: rx.redirect("/content/all/" + State.memoize_sort_by),
    )

    return rx.grid(
        rx.foreach(State.categories, category_button),
        all_button,
        columns="2",
        gap="10px",  # Add spacing between elements
        height="100vh",  # Take the whole height of the browser view
    )