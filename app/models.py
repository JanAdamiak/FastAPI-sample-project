import enum

from email.policy import default
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    SmallInteger,
    DateTime,
    Enum,
)
from sqlalchemy.sql import func

from .database import Base


class RegionalOffice(Base):
    __tablename__ = "regional_offices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    is_active = Column(Boolean, default=True)
    last_login: Column(DateTime(timezone=True))
    username: str
    password: str
    client_id: str
    client_secret: str


class Purchase(Base):
    class StateOfPurchase(enum.Enum):
        ORDER_PAID = "Order has been paid"
        MANUFACTURING_INITIATED = "Manufacturing initiated"
        ORDER_FULFILLED = "Order has been fulfilled"

    class BrandOfCar(enum.Enum):
        TOYOTA = "Toyota"
        LEXUS = "Lexus"
        HONDA = "Honda"

    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    regional_office = Column(Integer, ForeignKey("regional_offices.id"))
    external_order_number = Column(String)
    car_model = Column(String)
    brand = Column(Enum(BrandOfCar))
    state = Column(Enum(StateOfPurchase))
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    timestamp_manufacturing_started = Column(DateTime(timezone=True), default=None)
    timestamp_order_fulfilled = Column(DateTime(timezone=True), default=None)
