import reflex as rx

@rx.page(route="/")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.button(
                rx.flex(
                    rx.icon("arrow-down-a-z", stroke_width=2.5, size=30, margin_right="20px"),
                    rx.text("Inhoud per category", weight="medium"),
                    align="center",
                ),
                color_scheme="indigo",
                width="100vw",  # Full width
                height="32vh",  # 1/4 of screen height
                font_size="2em",  # Increase font size
            ),
            rx.button(
                rx.flex(
                    rx.icon("arrow-down-narrow-wide", stroke_width=2.5, size=30, margin_right="20px"),
                    rx.text("Inhoud per vervaldatum", weight="medium"),
                    align="center",
                ),
                color_scheme="indigo",
                width="100vw",
                height="32vh",
                font_size="2em",  # Increase font size
            ),
            rx.button(
                rx.flex(
                    rx.icon("plus", stroke_width=2.5, size=30, margin_right="20px"),
                    rx.text("Toevoegen", weight="medium"),
                    align="center",
                ),
                color_scheme="teal",
                width="100vw",
                height="32vh",
                font_size="2em",  # Increase font size
                on_click=lambda: rx.redirect("/add"),
            ),
            align="center",
            width="100%",
            # padding=0,  # Remove extra padding
        ),
        width="100vw",
        height="100vh",  # Make sure the whole screen is filled
    )

