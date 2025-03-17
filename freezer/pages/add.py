import reflex as rx

@rx.page(route="/add")
def add_product() -> rx.Component:
    # categories = get_categories()
    categories = []
    return rx.center(
        rx.vstack(
            rx.input(
                placeholder="Productnaam",
                id="article",
            ),
            rx.select(
                items=categories,
                placeholder="Categorie",
                id="category",
            ),
            rx.input(
                placeholder="Vervaldatum (dagen)",
                id="expiration_date",
            ),
            rx.text_area(
                placeholder="Type extra info hier...",
                id="comment",
            ),
            # rx.button("Toevoegen", on_click=lambda: add_product_to_api(
            #     rx.get_value("category"),
            #     rx.get_value("article"),
            #     rx.get_value("expiration_date"),
            #     rx.get_value("comment")
            # ) and rx.redirect("/")),
            rx.button("Terug", on_click=lambda: rx.redirect("/")),
            align="center",
            width="100%",
            padding=4,
        )
    )