import reflex as rx
import requests


# Function to fetch categories from API
def get_categories():
    try:
        response = requests.get("http://localhost:8000/listCategories")
        categories = response.json()
        print(categories)
        return [category["category"] for category in categories]
    except Exception:
        return []  # Return empty list on failure


# Function to add a product by sending a POST request
def add_product_to_api(category, article, expiration_date, comment):
    try:
        response = requests.post(
            "http://localhost:8000/addItem",
            json={
                "category": category,
                "article": article,
                "expiration_date": expiration_date,
                "comment": comment,
            },
        )
        return response.status_code == 200
    except Exception:
        return False


# PAGES
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


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="sky",
        gray_color="auto",
        scaling="110%",
        radius="large",
    )
)
app.add_page(index, title="Freezer")
app.add_page(add_product, route="/add", title="Toevoegen Product")
