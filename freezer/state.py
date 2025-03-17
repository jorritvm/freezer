import logging

import reflex as rx
from sqlmodel import select

from .models import Category, DefaultExpiration, FreezerContent

# Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

class State(rx.State):
    categories: list[str] = []

    @rx.event
    def list_categories(self):
        with rx.session() as session:
            query_result = session.exec(select(Category).order_by(Category.category)).all()
            # logger.debug(f"Query result: {query_result}")
            self.categories =  sorted([category.category for category in query_result])
            # logger.debug(f"Categories: {self.categories}")