from datetime import datetime, timedelta
import logging

import reflex as rx
from .models import Category, DefaultExpiration, FreezerContent

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class State(rx.State):
    categories: list[str] = []
    contents: list[FreezerContent] = []

    @rx.event
    def list_categories(self):
        with rx.session() as session:
            query_result = session.exec(Category.select().order_by(Category.category)).all()
            # logger.debug(f"Query result: {query_result}")
            self.categories =  sorted([category.category for category in query_result])
            # logger.debug(f"Categories: {self.categories}")

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
            self.contents = list(query_result)

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