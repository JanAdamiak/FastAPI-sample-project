from datetime import datetime
from sqlalchemy.orm import Session

from .models import Purchase, RegionalOffice
from .schemas import PurchaseCreate, PurchaseUpdate, RegionalOfficeCreate


def get_purchase_by_id(db: Session, purchase_id: int):
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()


def create_purchase(db: Session, purchase: PurchaseCreate):
    db_regional_office = get_regional_office_by_id(db, purchase.regional_office)
    if not db_regional_office:
        return

    db_purchase = Purchase(**purchase.dict(), state=Purchase.StateOfPurchase.ORDER_PAID)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase


def update_purchase(db: Session, purchase_id: int, purchase: PurchaseUpdate):
    db_purchase = get_purchase_by_id(db, purchase_id)
    if not db_purchase:
        return

    # Checks for state changes
    if db_purchase.state != purchase.state:
        if purchase.state == Purchase.StateOfPurchase.MANUFACTURING_INITIATED:
            db_purchase.timestamp_manufacturing_started = datetime.utcnow()
        elif purchase.state == Purchase.StateOfPurchase.ORDER_FULFILLED:
            db_purchase.timestamp_order_fulfilled = datetime.utcnow()
        # Updating of the state
        db_purchase.state = purchase.state

        db.commit()
        db.refresh(db_purchase)
    return db_purchase


def get_unmanufactured_purchases_by_brand(db: Session, brand: Purchase.BrandOfCar):
    return (db.query(Purchase).filter(Purchase.state == Purchase.StateOfPurchase.ORDER_PAID,Purchase.brand == brand,).all())


def create_regional_office(db: Session, regional_office: RegionalOfficeCreate):
    db_regional_office = RegionalOffice(**regional_office.dict())
    db.add(db_regional_office)
    db.commit()
    db.refresh(db_regional_office)
    return db_regional_office


def get_regional_office_by_id(db: Session, regional_office_id: int):
    return db.query(RegionalOffice).filter(RegionalOffice.id == regional_office_id).first()
