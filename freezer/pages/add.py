import reflex as rx
from ..state import State

@rx.page(route="/add")
def add_product() -> rx.Component:
    # categories = get_categories()
    return rx.vstack(
            rx.input(
                placeholder="Productnaam",
                name="article",
                width="100vw",  # Full width
            ),
            rx.select(
                items=State.categories,
                placeholder="Categorie",
                name="category",
                width="100vw",  # Full width
            ),
            rx.input(
                placeholder="Vervaldatum (dagen)",
                name="expiration_date",
                type="number",
                min=1,
                width="100vw",  # Full width
            ),
            rx.text_area(
                placeholder="Type extra info hier...",
                name="comment",
                width="100vw",  # Full width
                height="40vh",
            ),
            rx.button(
                "Toevoegen",
                #       on_click=lambda: add_product_to_api(
                # rx.get_value("category"),
                # rx.get_value("article"),
                # rx.get_value("expiration_date"),
                # rx.get_value("comment") ) and rx.redirect("/")
                width="100vw",
                height="10vh",
            ),
            rx.button(
                "Terug",
                on_click=lambda: rx.redirect("/"),
                width="100vw",
                height="10vh", ),
            align="center",
            width="100%",
            padding=4,
        )