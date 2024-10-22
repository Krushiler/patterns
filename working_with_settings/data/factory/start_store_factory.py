from datetime import datetime

from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType


class StartStoreFactory:
    def __init__(self, nomenclatures_factory: StartNomenclatureFactory):
        self._nomenclatures_factory = nomenclatures_factory

    @lazy
    def stores(self) -> list[Store]:
        return [
            Store('Москва, ул. Ленина, 7'),
            Store('Новосибирск, ул. Кирова, 15'),
        ]

    @lazy
    def store_transactions(self) -> list[StoreTransaction]:
        wheat_flour = self._nomenclatures_factory.wheat_flour()
        milk = self._nomenclatures_factory.milk()

        return [
            StoreTransaction(
                store=self.stores()[0],
                nomenclature=wheat_flour,
                amount=MeasuredValue(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.INCOME,
                time=datetime(2020, 1, 1, 1, 5, 9)
            ),
            StoreTransaction(
                store=self.stores()[1],
                nomenclature=wheat_flour,
                amount=MeasuredValue(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 3, 6, 3, 7)
            ),
            StoreTransaction(
                store=self.stores()[0],
                nomenclature=wheat_flour,
                amount=MeasuredValue(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
            StoreTransaction(
                store=self.stores()[1],
                nomenclature=milk,
                amount=MeasuredValue(1.0, milk.unit),
                transaction_type=StoreTransactionType.INCOME,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
            StoreTransaction(
                store=self.stores()[0],
                nomenclature=milk,
                amount=MeasuredValue(1.0, milk.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
        ]
