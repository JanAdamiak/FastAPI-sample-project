import pytest
from pydantic.error_wrappers import ValidationError

from ..schemas import PurchaseCreate, PurchaseUpdate, RegionalOfficeCreate
from ..models import Purchase
from ..crud import create_purchase, update_purchase, create_regional_office


class TestCrudCommands:
    def test_purchase_creation_failed_no_regional_office_attached(self, session):
        purchase_schema = PurchaseCreate(regional_office=1, external_order_number="78NFO8F7V87TI7", car_model="Corolla", brand=Purchase.BrandOfCar.TOYOTA)
        purchase_object = create_purchase(session, purchase_schema)
        assert not purchase_object


    def test_purchase_creation(self, session):
        regional_office_schema = RegionalOfficeCreate(name="test office", location="here", username='testuser', password="sdlkgjhrwsogh45e9iuth9375v8yq6983qu98y49836yq9c349y8c594832yqc")
        regional_office = create_regional_office(session, regional_office_schema)

        assert regional_office

        purchase_schema = PurchaseCreate(regional_office=regional_office.id, external_order_number="78NFO8F7V87TI7", car_model="Corolla", brand=Purchase.BrandOfCar.TOYOTA)
        purchase_object = create_purchase(session, purchase_schema)

        assert purchase_object.regional_office == regional_office.id
        assert purchase_object.external_order_number == "78NFO8F7V87TI7"
        assert purchase_object.car_model == "Corolla"
        assert purchase_object.brand == Purchase.BrandOfCar.TOYOTA
        assert purchase_object.state == Purchase.StateOfPurchase.ORDER_PAID
        assert purchase_object.time_created
        assert purchase_object.timestamp_manufacturing_started is None
        assert purchase_object.timestamp_order_fulfilled is None


    def test_invalid_purchase_creation(self, session):
        with pytest.raises(ValidationError):
            purchase_schema = PurchaseCreate(regional_office=1, external_order_number="123", car_model="123", brand="FakeBrand")
            create_purchase(session, purchase_schema)


    def test_purchase_update(self, session):
        regional_office_schema = RegionalOfficeCreate(name="test office", location="here", username='testuser', password="sdlkgjhrwsogh45e9iuth9375v8yq6983qu98y49836yq9c349y8c594832yqc")
        regional_office = create_regional_office(session, regional_office_schema)

        assert regional_office

        purchase_schema = PurchaseCreate(regional_office=regional_office.id, external_order_number="2315423513", car_model="TestCar", brand=Purchase.BrandOfCar.TOYOTA)
        purchase_object = create_purchase(session, purchase_schema)

        assert purchase_object.state == Purchase.StateOfPurchase.ORDER_PAID
        assert purchase_object.timestamp_manufacturing_started is None

        new_purchase_schema = PurchaseUpdate(state=Purchase.StateOfPurchase.MANUFACTURING_INITIATED)
        purchase_object = update_purchase(session, purchase_object.id, new_purchase_schema)

        assert purchase_object.state == Purchase.StateOfPurchase.MANUFACTURING_INITIATED
        assert purchase_object.timestamp_manufacturing_started
        assert purchase_object.timestamp_order_fulfilled is None

        new_purchase_schema = PurchaseUpdate(state=Purchase.StateOfPurchase.ORDER_FULFILLED)
        purchase_object = update_purchase(session, purchase_object.id, new_purchase_schema)

        assert purchase_object.state == Purchase.StateOfPurchase.ORDER_FULFILLED
        assert purchase_object.timestamp_manufacturing_started
        assert purchase_object.timestamp_order_fulfilled

    def test_purchase_update_object_not_found(self, session):
        new_purchase_schema = PurchaseUpdate(state=Purchase.StateOfPurchase.MANUFACTURING_INITIATED)
        purchase_object = update_purchase(session, 10000000000, new_purchase_schema)

        assert purchase_object is None
