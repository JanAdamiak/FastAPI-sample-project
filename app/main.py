import http
import logging

from fastapi import Depends, FastAPI, HTTPException, Request, Response, Header
from sqlalchemy.orm import Session

from .utils import add_purchase_task, update_state, get_db
from .schemas import PurchaseCreate, PurchaseUpdate
from .models import Base, Purchase
from .database import engine
from .crud import get_unmanufactured_purchases_by_brand

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/v1/sales-webhook")
def sales_webhook(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    add_purchase_task(purchase, db)
    return {}


@app.post("/v1/update-state-webhook/{purchase_id}")
def update_state_webhook(purchase: PurchaseUpdate, purchase_id: int, db: Session = Depends(get_db)):
    purchase_object = update_state(purchase, purchase_id, db)
    if purchase_object is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase_object


@app.get("/v1/get-all-vehicles-for-manufacturing/{brand}")
def update_state_webhook(brand: Purchase.BrandOfCar, db: Session = Depends(get_db)):
    return get_unmanufactured_purchases_by_brand(db, brand)
