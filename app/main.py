import http
import logging

from fastapi import Depends, FastAPI, HTTPException, Request, Response, Header
from sqlalchemy.orm import Session

from .utils import add_purchase_task, update_state_task, get_db
from .crud import get_purchase_by_id
from .schemas import Purchase, PurchaseCreate
from .models import Base
from .database import engine

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/v1/sales-webhook")
def sales_webhook(purchase: PurchaseCreate, request: Request, x_token: str | None = Header(default=None), db: Session = Depends(get_db)):
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print(x_token)
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print(request)
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print(db)
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    # add_purchase_task()
    return {}


@app.post("/v1/update-state-webhook/{purchase_id}")
def update_state_webhook(purchase_id: int, request: Request):
    print(request)
    print(update_state_task)
    return {"test": "test"}


@app.get("/v1/get-all-vehicles-for-manufacturing")
def update_state_webhook(request: Request):
    print(request)
    return {"test": "test"}
