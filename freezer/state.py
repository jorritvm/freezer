from dataclasses import dataclass
from datetime import datetime, timedelta
import logging

import reflex as rx
from .models import Category, DefaultExpiration, FreezerContent

# configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# set up dataclasses that extend the SQL models and will be stored in the app state
@dataclass
class FreezerContentState:
    """Wrapper around FreezerContent that includes an expiration status."""
    id: int
    category: str
    article: str
    add_date: str
    expiration_date: str
    comment: str
    expired_status: str

# define the app state and event handlers
class State(rx.State):
    categories: list[str] = []
    contents: list[FreezerContentState] = []

    @rx.event
    def list_categories(self):
        logger.debug(f"Listing categories")
        with rx.session() as session:
            query_result = session.exec(Category.select().order_by(Category.category)).all()
            self.categories =  sorted([category.category for category in query_result])
            logger.debug(f"Categories: {self.categories}")

    @rx.event
    def list_contents(self):
        logger.debug(f"Listing contents for category: {self.category}")
        category = self.category
        with (rx.session() as session):
            if not category or category == "all":
                query_result = session.exec(FreezerContent.select().order_by(FreezerContent.article)).all()
            else:
                query_result = session.exec(FreezerContent.select().where(FreezerContent.category == category).order_by(FreezerContent.article)).all()
            logger.debug(f"Query result returns {len(query_result)} items")

            self.contents = [
                FreezerContentState(
                    id=article.id,
                    category=article.category,
                    article=article.article,
                    add_date=article.add_date,
                    expiration_date=article.expiration_date,
                    comment=article.comment,
                    expired_status=compute_expiration_status(article.expiration_date)
                )
                for article in query_result
            ]

    @rx.event
    def add_article(self, form_data: dict):
        logger.debug(f"Adding article from form data: {form_data}")
        if not form_data:
            return
        if form_data['article'] is None or  form_data['article'] == "":
            return

        # add the article
        current_date = datetime.now().date()
        current_date_iso_str = current_date.isoformat()
        expiration_date = current_date + timedelta(days=int(form_data["expiration_date"]))
        expiration_date_str = expiration_date.isoformat()
        with rx.session() as session:
            new_article = FreezerContent(category=form_data['category'],
                                         article=form_data['article'],
                                         add_date=current_date_iso_str,
                                         expiration_date=expiration_date_str,
                                         comment=form_data['comment'])
            session.add(new_article)
            session.commit()
            logger.debug(f"Added article: {new_article}")

        # upsert this new expiration date into the default expiration table
        this_article_expiration = DefaultExpiration(category=form_data['category'],
                                                    article=form_data['article'],
                                                    expiration_duration=int(form_data['expiration_date']))

        with rx.session() as session:
            existing_expiration = session.exec(DefaultExpiration.select().where((DefaultExpiration.category == form_data['category']) & (DefaultExpiration.article == form_data['article']))).first()
            logger.debug(f"Existing expiration: {existing_expiration}")
            if existing_expiration:
                existing_expiration.expiration_duration = int(form_data['expiration_date'])
                session.commit()
                logger.debug(f"Updated expiration: {existing_expiration}")
            else:
                session.add(this_article_expiration)
                session.commit()
                logger.debug(f"Added expiration: {this_article_expiration}")

    @rx.event
    def remove_article(self, item_id: int):
        """Remove an item by its ID."""
        with rx.session() as session:
            article_to_remove = session.exec(FreezerContent.select().where(FreezerContent.id == item_id)).first()
            if article_to_remove:
                session.delete(article_to_remove)
                session.commit()
                logger.debug(f"Removed article with id {item_id}")
        self.contents = [item for item in self.contents if item.id != item_id]

# helpers
def compute_expiration_status(expiration_date: str) -> str:
    """Determine if an item is expired, almost expired, or good."""
    today = datetime.now().date()
    expiration_date = datetime.fromisoformat(expiration_date).date()

    if expiration_date < today:
        return "expired"
    elif (expiration_date - today).days <= 10:  # Less than x days remaining
        return "almost"
    return "good"