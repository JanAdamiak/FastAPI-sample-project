import logging

from sqlalchemy.orm import Session

from .schemas import PurchaseCreate, PurchaseUpdate
from .database import SessionLocal
from .crud import get_purchase_by_external_order_number_and_regional_office, create_purchase, update_purchase

logger = logging.getLogger(__name__)


def add_purchase_task(purchase: PurchaseCreate, db: Session):
    """
    This is a wrapper function for a Celery task.
    """
    logger.info("add_purchase_task() queuing a new add_purchase task")
    # This will use celery to spawn a task
    add_purchase(purchase, db)


def add_purchase(purchase: PurchaseCreate, db: Session):
    db_purchase = get_purchase_by_external_order_number_and_regional_office(db, purchase)
    if db_purchase:
        logger.warning("add_purchase() purchase already exists with external order number %s and regional office %s", (purchase.external_order_number, purchase.regional_office))
        return
    purchase_object = create_purchase(db, purchase)
    logger.info("add_purchase() adding new purchase with external order number %s and regional office %s. New id is: %s", (purchase.external_order_number, purchase.regional_office, purchase_object.id))


def update_state(purchase: PurchaseUpdate, purchase_id: int, db: Session):
    db_purchase_object = update_purchase(db, purchase_id, purchase)
    if not db_purchase_object:
        logger.warning("update_state() purchase with this id doesn't exists")
        return
    logger.info("update_state() updating purchase state with id %s", (db_purchase_object.id,))
    return db_purchase_object


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
