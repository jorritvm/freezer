from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from .crud import add_item, remove_item, list_items, list_categories
from .crud import get_db

app = FastAPI()

@app.post("/addItem")
async def add_item_endpoint(category: str, article: str, expiration_date: str, comment: str, db: Session = Depends(get_db)):
    try:
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    await add_item(db, category, article, expiration_date_obj, comment)
    return {"message": "Item added successfully"}

@app.delete("/removeItem")
async def remove_item_endpoint(category: str, article: str, add_date: str, db: Session = Depends(get_db)):
    try:
        add_date_obj = datetime.strptime(add_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    await remove_item(db, category, article, add_date_obj)
    return {"message": "Item removed successfully"}

@app.get("/listItems")
async def list_items_endpoint(db: Session = Depends(get_db)):
    items = await list_items(db)
    return items

@app.get("/listCategories")
async def list_categories_endpoint(db: Session = Depends(get_db)):
    categories = await list_categories(db)
    return categories