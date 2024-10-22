from datetime import datetime

import pytest

from working_with_settings.di.di import Di
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType
from working_with_settings.domain.process.store.turnovers_from_transactions_process import \
    TurnoversFromTransactionsProcess


@pytest.fixture
def store(inject: Di) -> Store:
    return inject.get_start_store_factory().stores()[0]


@pytest.fixture
def store_nomenclature(inject: Di) -> Nomenclature:
    return inject.get_start_nomenclature_factory().sugar()


@pytest.fixture
def transactions(store, store_nomenclature) -> list[StoreTransaction]:
    return [
        StoreTransaction(
            store=store,
            nomenclature=store_nomenclature,
            amount=MeasuredValue(50.0, store_nomenclature.unit),
            transaction_type=StoreTransactionType.INCOME,
            time=datetime(2020, 1, 1, 1, 5, 9)
        ),
        StoreTransaction(
            store=store,
            nomenclature=store_nomenclature,
            amount=MeasuredValue(25.0, store_nomenclature.unit),
            transaction_type=StoreTransactionType.EXPENSE,
            time=datetime(2020, 1, 3, 6, 3, 7)
        ),
    ]


def test_turnover_calculation(transactions, inject: Di):
    process = TurnoversFromTransactionsProcess()
    turnover = process.calculate(transactions)

    assert turnover[0].turnover == MeasuredValue(25.0, inject.get_measurement_units_factory().kilograms())


def test_turnover_calculation_with_different_nomenclature(transactions, inject: Di):
    process = TurnoversFromTransactionsProcess()

    transactions.append(
        StoreTransaction(
            store=transactions[0].store,
            nomenclature=inject.get_start_nomenclature_factory().milk(),
            amount=MeasuredValue(1.0, inject.get_measurement_units_factory().liter()),
            transaction_type=StoreTransactionType.EXPENSE,
            time=datetime(2020, 1, 5, 5, 8, 2)
        )
    )

    turnover = process.calculate(transactions)

    assert len(turnover) == 2
    assert turnover[0].turnover == MeasuredValue(25.0, inject.get_measurement_units_factory().kilograms())
    assert turnover[1].turnover == MeasuredValue(-1.0, inject.get_measurement_units_factory().liter())
