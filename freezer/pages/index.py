import reflex as rx

@rx.page(route="/")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.button(
                "Inhoud per categorie",
            ),
            rx.button(
                "Inhoud per vervaldatum",
            ),
            rx.button(
                "Toevoegen",
                on_click=lambda: rx.redirect("/add"),
            ),
            align="center",
            width="100%",
            padding=4,
        )
    )