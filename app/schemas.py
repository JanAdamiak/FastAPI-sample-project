from datetime import datetime
from pydantic import BaseModel

from .models import Purchase


class PurchaseBase(BaseModel):
    regional_office: int
    external_order_number: str
    car_model: str
    brand: Purchase.BrandOfCar


class PurchaseCreate(PurchaseBase):
    pass


class PurchaseUpdate(BaseModel):
    state: Purchase.StateOfPurchase


class Purchase(PurchaseBase):
    id: int
    state: Purchase.StateOfPurchase
    time_created: datetime = None
    timestamp_manufacturing_started: datetime = None
    timestamp_order_fulfilled: datetime = None

    class Config:
        orm_mode = True


class RegionalOfficeBase(BaseModel):
    name: str
    location: str
    token_identification_to_change_name: str
    is_active: bool = True


class RegionalOfficeCreate(RegionalOfficeBase):
    pass


class RegionalOffice(RegionalOfficeBase):
    id: int

    class Config:
        orm_mode = True
