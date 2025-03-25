import reflex as rx
from ..state import State

@rx.page(route="/add", on_load=State.on_load_add())
def add_product() -> rx.Component:
    return rx.vstack(
            rx.form(
                rx.select(
                    items=State.categories,
                    placeholder="Categorie",
                    name="category",
                    value=State.add_category,
                    on_change=lambda value: State.set_add_category(value),
                    width="100vw",
                ),
                rx.input(
                    placeholder="Artikel",
                    name="article",
                    value=State.add_article,
                    on_change=lambda value: State.set_add_article(value),
                    width="100vw",
                ),
                rx.input(
                    placeholder="Vervaldatum (dagen)",
                    name="expiration_date",
                    value=State.add_expiration_date,
                    on_change=lambda value: State.set_add_expiration_date(value),
                    width="100vw",
                ),
                rx.input(
                    placeholder="Hoeveelheid",
                    name="quantity",
                    value=State.add_quantity,
                    on_change=lambda value: State.set_add_quantity(value),
                    width="100vw",
                ),
                rx.text_area(
                    placeholder="Type extra info hier...",
                    name="comment",
                    value=State.add_comment,  # Use state variable
                    on_change=lambda value: State.set_add_comment(value),
                    width="100vw",
                    height="30vh",
                ),
                rx.button(
                    "Toevoegen",
                    width="100vw",
                    height="10vh",
                ),
            on_submit=State.handle_add_article,
            ),
            rx.button(
                "Terug",
                on_click=lambda: rx.redirect("/"),
                width="100vw",
                height="10vh",
            ),
            rx.text(State.add_validation),
            align="center",
            width="100%",
            padding=4,
    )