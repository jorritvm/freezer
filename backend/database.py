import os

from sqlalchemy import create_engine, Column, String, Date, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    f"sqlite:///{os.path.join(os.getcwd(), 'backend', 'database', 'freezer.db')}"
)
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    category = Column(String, primary_key=True, unique=True, index=True)


class FreezerContent(Base):
    __tablename__ = "freezer_contents"
    category = Column(String, primary_key=True)
    article = Column(String, primary_key=True)
    add_date = Column(Date, primary_key=True)
    expiration_date = Column(Date)
    comment = Column(String)


class DefaultExpiration(Base):
    __tablename__ = "default_expiration_date"
    category = Column(String, primary_key=True)
    article = Column(String, primary_key=True)
    expiration_duration = Column(Integer)


def create_default_categories():
    categories = ["vis", "vlees", "groenten", "soep", "ijs", "oven"]
    print("trying to add categories")
    session = SessionLocal()
    for category in categories:
        if not session.query(Category).filter_by(category=category).first():
            session.add(Category(category=category))
            print("Added category: ", category)
    session.commit()
    session.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    create_default_categories()

