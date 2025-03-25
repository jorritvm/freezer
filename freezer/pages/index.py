import reflex as rx

@rx.page(route="/")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.button(
                rx.flex(
                    rx.icon("arrow-down-narrow-wide", stroke_width=2.5, size=30, margin_right="20px"),
                    rx.text("Inhoud", weight="medium"),
                    align="center",
                ),
                color_scheme="indigo",
                width="100vw",
                height="40dvh",
                font_size="2em",  # Increase font size
                on_click=lambda: rx.redirect("/content/all/expiration_date"),
            ),
            rx.button(
                rx.flex(
                    rx.icon("plus", stroke_width=2.5, size=30, margin_right="20px"),
                    rx.text("Toevoegen", weight="medium"),
                    align="center",
                ),
                color_scheme="teal",
                width="100vw",
                height="40dvh",
                font_size="2em",  # Increase font size
                on_click=lambda: rx.redirect("/add"),
            ),
            align="center",
            width="100%",
        ),
        width="100vw",
        height="100vh",
    )

