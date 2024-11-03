from datetime import datetime

from working_with_settings.data.factory.start_store_factory import StartStoreFactory
from working_with_settings.data.storage.store_storage import StoreStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction
from working_with_settings.domain.model.store.store_turnover import StoreTurnover
from working_with_settings.domain.prototype.store.turnovers_from_transactions_prototype import \
    TurnoversFromTransactionsPrototype


class StoreRepository:
    def __init__(self, store_transaction_storage: StoreTransactionStorage, store_storage: StoreStorage,
                 start_store_factory: StartStoreFactory):
        self._store_transaction_storage = store_transaction_storage
        self._store_storage = store_storage
        self._start_store_factory = start_store_factory

    def init_start_stores(self):
        if self._store_storage.is_empty():
            for store in self._start_store_factory.stores():
                self._store_storage.create(store)

        if self._store_transaction_storage.is_empty():
            for transaction in self._start_store_factory.store_transactions():
                self._store_transaction_storage.create(transaction)

    def get_stores(self, filters: list[Filter]) -> list[Store]:
        return self._store_storage.get_filtered(filters)

    def get_store_transactions(self, filters: list[Filter]) -> list[StoreTransaction]:
        return self._store_transaction_storage.get_filtered(filters)

    def get_turnovers(self, filters: list[Filter], grouping: list[str]) -> list[StoreTurnover]:
        transactions = self._store_transaction_storage.get_filtered(filters)
        return TurnoversFromTransactionsPrototype().calculate(transactions, grouping)
