import random
import time
from datetime import datetime

import pytest

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.data.storage.filterer.list_filterer import ListFilterer
from working_with_settings.di.di import Di
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.filter.range_model import RangeModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType
from working_with_settings.domain.model.store.store_turnover import StoreTurnover
from working_with_settings.domain.prototype.store.turnovers_from_transactions_prototype import \
    TurnoversFromTransactionsPrototype


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


@pytest.fixture
def generated_transactions(inject: Di) -> list[StoreTransaction]:
    stores = inject.get_start_store_factory().stores()
    result = []
    for i in range(10000):
        transaction_type = random.randint(0, 1)
        if transaction_type == 0:
            transaction_type = StoreTransactionType.INCOME
        else:
            transaction_type = StoreTransactionType.EXPENSE
        result.append(
            StoreTransaction(
                store=stores[i % len(stores)],
                nomenclature=inject.get_start_nomenclature_factory().sugar(),
                amount=MeasuredValue(random.randint(1, 100), inject.get_measurement_units_factory().kilograms()),
                transaction_type=transaction_type,
                # time=datetime.fromtimestamp(random.randint(0, datetime.now().timestamp()))
                time=datetime.fromtimestamp(0)
            )
        )
    return result


def test_turnover_calculation(transactions, inject: Di):
    process = TurnoversFromTransactionsPrototype()
    turnover = process.calculate(transactions, ['nomenclature', 'store'])

    assert turnover[0].turnover == MeasuredValue(25.0, inject.get_measurement_units_factory().kilograms())


def test_turnover_calculation_with_different_nomenclature(transactions, inject: Di):
    process = TurnoversFromTransactionsPrototype()

    transactions.append(
        StoreTransaction(
            store=transactions[0].store,
            nomenclature=inject.get_start_nomenclature_factory().milk(),
            amount=MeasuredValue(1.0, inject.get_measurement_units_factory().liter()),
            transaction_type=StoreTransactionType.EXPENSE,
            time=datetime(2020, 1, 5, 5, 8, 2)
        )
    )

    turnover = process.calculate(transactions, ['nomenclature', 'store'])

    assert len(turnover) == 2
    assert turnover[0].turnover == MeasuredValue(25.0, inject.get_measurement_units_factory().kilograms())
    assert turnover[1].turnover == MeasuredValue(-1.0, inject.get_measurement_units_factory().liter())


def test_cached_calculation(generated_transactions, inject: Di):
    repo = inject.get_store_repository()

    for transaction in generated_transactions:
        inject.get_store_transaction_storage().create(transaction)

    t = time.process_time()
    no_caching_result = repo.get_turnovers(
        [Filter('time', RangeModel(datetime.fromtimestamp(0), datetime.now()), FilterType.BETWEEN)],
        StoreTurnover.default_grouping(), datetime.now())
    t1 = time.process_time() - t

    t = time.process_time()
    caching_result = repo.get_turnovers(
        [Filter('time', RangeModel(datetime.fromtimestamp(0), datetime.now()), FilterType.BETWEEN)],
        StoreTurnover.default_grouping(), datetime.now())
    t2 = time.process_time() - t

    print()

    print('Без кэша:', 'Время выполнения:', t1)
    print('С кэшем: ', 'Время выполнения:', t2)

    assert len(caching_result) == len(no_caching_result)
    assert t2 < t1
