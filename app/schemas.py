from datetime import datetime
from pydantic import BaseModel

from .models import Purchase as PurchaseModel


class PurchaseBase(BaseModel):
    regional_office: int
    external_order_number: str
    car_model: str
    brand: PurchaseModel.BrandOfCar


class PurchaseCreate(PurchaseBase):
    pass


class PurchaseUpdate(BaseModel):
    state: PurchaseModel.StateOfPurchase


class Purchase(PurchaseBase):
    id: int
    state: PurchaseModel.StateOfPurchase
    time_created: datetime = None
    timestamp_manufacturing_started: datetime = None
    timestamp_order_fulfilled: datetime = None

    class Config:
        orm_mode = True


class RegionalOfficeBase(BaseModel):
    name: str
    location: str
    is_active: bool = True
    username: str


class RegionalOfficeCreate(RegionalOfficeBase):
    password: str


class RegionalOffice(RegionalOfficeBase):
    id: int
    last_login: datetime = datetime.utcnow()

    class Config:
        orm_mode = True
