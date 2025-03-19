import reflex as rx
from ..state import State
from ..models import FreezerContent

@rx.page(route="/content/[category]", on_load=State.list_contents())
def content_by_category() -> rx.Component:
    """A page that updates based on the route."""
    # Displays the dynamic part of the URL, the post ID
    return rx.vstack(
        home_and_filter_buttons(),
        rx.foreach(State.contents, article_entry),
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

def article_entry(freezer_article: FreezerContent) -> rx.Component:
    background_color = rx.cond(
        freezer_article.expired_status == "expired",
        "lightcoral",
        rx.cond(
            freezer_article.expired_status == "almost",
            "yellow",
            "white"
        )
    )

    # Alert Dialog for confirmation
    dialog = rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.icon("circle-x", width="30px", cursor="pointer"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirm Deletion"),
            rx.alert_dialog.description(f"Are you sure you want to delete '{freezer_article.category}-{freezer_article.article}'?"),
            rx.flex(
                rx.alert_dialog.cancel(rx.button("Cancel", color_scheme="gray")),
                rx.alert_dialog.action(
                    rx.button("OK",
                        on_click=lambda: State.remove_article(freezer_article.id),
                        color_scheme="red"
                    ),
                ),
                spacing="3",
            ),
        ),
    )

    return rx.grid(
        rx.text(freezer_article.category, align_self="center"),  # Center vertically
        rx.text(freezer_article.article, align_self="center"),  # Center vertically
        rx.text(
            freezer_article.expiration_date,
            align_self="center",
            white_space="nowrap"  # Prevent wrapping
        ),
        rx.icon(
            "info",
            width="30px",
            cursor="pointer",
            on_click=lambda: rx.toast(freezer_article.comment),
            align_self="center",  # Center vertically
        ),
        rx.icon("pencil", width="30px", align_self="center"),  # Center vertically
        dialog,
        columns="1fr 3fr 2fr 30px 30px 30px",
        gap="10px",
        padding="10px",
        border="1px solid black",
        width="100%",
        bg=background_color,
        align_items="center",  # Ensure everything in the grid is centered vertically
    )
