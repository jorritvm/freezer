from datetime import date, datetime

from sqlalchemy.orm import Session

from .database import SessionLocal, FreezerContent, Category


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Freezer Contents CRUD operations
async def add_item(
    db: Session, category: str, article: str, expiration_date: date, comment: str
):
    # add the category if it did not exist yet
    if not db.query(Category).filter_by(category=category).first():
        db.add(Category(category=category))
    db.commit()

    # add the article to the freezer
    db_item = FreezerContent(
        category=category,
        article=article,
        add_date=datetime.today().date(),
        expiration_date=expiration_date,
        comment=comment,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def remove_item(db: Session, category: str, article: str, add_date: date):
    db_item = (
        db.query(FreezerContent)
        .filter_by(category=category, article=article, add_date=add_date)
        .first()
    )
    db.delete(db_item)
    db.commit()


async def list_items(db: Session):
    return db.query(FreezerContent).all()


async def list_categories(db: Session):
    return db.query(Category).all()