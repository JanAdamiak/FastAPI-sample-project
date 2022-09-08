import logging

from .database import SessionLocal

logger = logging.getLogger(__name__)


def add_purchase_task():
    """
    This is a wrapper function for a Celery task.
    """
    add_purchase()
    # If record already exists stop the functionality
    # Else proceed with creation of the purchase
    print("add_purchase_task")


def add_purchase():
    db_purchase = get_purchase_by_id(db, purchase_id=purchase.id)
    if db_purchase:
        logger.warning("")
        return
    print("add_purchase")


def update_state_task():
    """
    This is a wrapper function for a Celery task.
    """
    # If record already exists stop the functionality
    # Else proceed with creation of the purchase
    print("update_state")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
