import reflex as rx

class Category(rx.Model, table=True):
    category: str

class DefaultExpiration(rx.Model, table=True):
    category: str
    article: str
    expiration_duration: int

class FreezerContent(rx.Model, table=True):
    category: str
    article: str
    add_date: str
    expiration_date: str
    comment: str