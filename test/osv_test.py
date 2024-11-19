import datetime
import uuid

import pytest

from working_with_settings.application.organization.store_manager import StoreManager
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.di.di import Di
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.filter.range_model import RangeModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType


@pytest.fixture
def nomenclature(inject: Di) -> Nomenclature:
    return inject.get_start_nomenclature_factory().wheat_flour()


@pytest.fixture
def store() -> Store:
    return Store(address='test')


def test_osv_calculation(inject: Di, nomenclature: Nomenclature, store):
    # Arrange

    transaction_storage: StoreTransactionStorage = inject.get_store_transaction_storage()
    store_manager: StoreManager = inject.get_store_manager()

    transaction_storage.create(
        StoreTransaction(
            store=store,
            nomenclature=nomenclature,
            amount=MeasuredValue(
                value=10,
                unit=nomenclature.unit
            ),
            transaction_type=StoreTransactionType.INCOME,
            time=datetime.datetime.fromtimestamp(1000000, tz=datetime.timezone.utc)
        )
    )

    transaction_storage.create(
        StoreTransaction(
            store=store,
            nomenclature=nomenclature,
            amount=MeasuredValue(
                value=3,
                unit=nomenclature.unit
            ),
            transaction_type=StoreTransactionType.EXPENSE,
            time=datetime.datetime.fromtimestamp(5000000, tz=datetime.timezone.utc)
        )
    )

    transaction_storage.create(
        StoreTransaction(
            store=store,
            nomenclature=nomenclature,
            amount=MeasuredValue(
                value=2,
                unit=nomenclature.unit
            ),
            transaction_type=StoreTransactionType.EXPENSE,
            time=datetime.datetime.fromtimestamp(5000000, tz=datetime.timezone.utc)
        )
    )

    # Act

    reports = store_manager.get_osv_nomenclature_reports(
        start_date=datetime.datetime.fromtimestamp(2500000, tz=datetime.timezone.utc),
        end_date=datetime.datetime.now(),
        store_id=store.id,
        blocking_date=datetime.datetime.now()
    )

    report = reports[0]

    # Assert

    assert len(reports) == 1

    assert report.nomenclature.id == nomenclature.id
    assert report.start_amount == MeasuredValue(value=10, unit=nomenclature.unit)
    assert report.end_amount == MeasuredValue(value=5, unit=nomenclature.unit)
