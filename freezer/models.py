# populate_data.py
import reflex as rx
from sqlmodel import Session, select


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


##############################

def populate_default_categories():
    default_categories = ["vis", "vlees", "gevogelte", "groenten", "brood", "ijs", "klaargemaakt"]

    with rx.session() as session:
        # Check if the data already exists
        existing_data = session.exec(select(Category)).all()
        if not existing_data:
            # Insert the default data
            for dc in default_categories:
                session.add(Category(category=dc))
            session.commit()
            print("Categories: Default data populated successfully.")
        else:
            print("Categories: Default data already exists.")

def populate_default_expiration():
    default_expiration = {
        "vis": 3*30,
        "vlees": 9*30,
        "gevogelte": 3*30,
        "groenten": 12*30,
        "brood": 1*30,
        "ijs": 12*30,
        "klaargemaakt": 3*30
    }

    with rx.session() as session:
        # Check if the data already exists
        existing_data = session.exec(select(DefaultExpiration)).all()
        if not existing_data:
            # Insert the default data
            for category,expiration in default_expiration.items():
                session.add(DefaultExpiration(category=category, article="all", expiration_duration=expiration))
            session.commit()
            print("Default Expiration: Default data populated successfully.")
        else:
            print("Default Expiration: Default data already exists.")

if __name__ == "__main__":
    populate_default_categories()
    populate_default_expiration()