import reflex as rx

# # Function to fetch categories from API
# def get_categories():
#     try:
#         response = requests.get("http://localhost:8000/listCategories")
#         categories = response.json()
#         print(categories)
#         return [category["category"] for category in categories]
#     except Exception:
#         return []  # Return empty list on failure
#
#
# # Function to add a product by sending a POST request
# def add_product_to_api(category, article, expiration_date, comment):
#     try:
#         response = requests.post(
#             "http://localhost:8000/addItem",
#             json={
#                 "category": category,
#                 "article": article,
#                 "expiration_date": expiration_date,
#                 "comment": comment,
#             },
#         )
#         return response.status_code == 200
#     except Exception:
#         return False




app = rx.App(
    # theme=rx.theme(
    #     appearance="light",
    #     accent_color="sky",
    #     gray_color="auto",
    #     scaling="110%",
    #     radius="large",
    # )
)
# app.add_page(index, title="Freezer")
# app.add_page(add_product, route="/add", title="Toevoegen Product")
