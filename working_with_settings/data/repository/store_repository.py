import datetime
from copy import deepcopy

from working_with_settings.data.factory.start_store_factory import StartStoreFactory
from working_with_settings.data.storage.filterer.list_filterer import ListFilterer
from working_with_settings.data.storage.store_storage import StoreStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.data.storage.turnover_storage import TurnoverStorage
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.filter.filter_utils import FilterUtils
from working_with_settings.domain.model.store.store import Store
from working_with_settings.domain.model.store.store_transaction import StoreTransaction
from working_with_settings.domain.model.store.store_turnover import StoreTurnover
from working_with_settings.domain.prototype.store.turnovers_from_transactions_prototype import \
    TurnoversFromTransactionsPrototype


class StoreRepository:
    def __init__(self,
                 store_transaction_storage: StoreTransactionStorage,
                 store_storage: StoreStorage,
                 turnover_storage: TurnoverStorage,
                 start_store_factory: StartStoreFactory
                 ):
        self._store_transaction_storage = store_transaction_storage
        self._store_storage = store_storage
        self._turnover_storage = turnover_storage
        self._start_store_factory = start_store_factory

    def init_start_stores(self):
        if self._store_storage.is_empty():
            for store in self._start_store_factory.stores():
                self._store_storage.create(store)

        if self._store_transaction_storage.is_empty():
            for transaction in self._start_store_factory.store_transactions():
                self._store_transaction_storage.create(transaction)

    def update_transaction(self, transaction_id: str, transaction: StoreTransaction):
        self._store_transaction_storage.update(transaction_id, transaction)

    def get_stores(self, filters: list[Filter]) -> list[Store]:
        return self._store_storage.get_filtered(filters)

    def get_store_transactions(self, filters: list[Filter]) -> list[StoreTransaction]:
        return self._store_transaction_storage.get_filtered(filters)

    def get_turnovers(self, filters: list[Filter], grouping: list[str], blocking_date: datetime.datetime) \
            -> list[StoreTurnover]:

        time_filter = FilterUtils.find_filter(filters, 'time', FilterType.BETWEEN)

        if time_filter.value.from_value is not None and time_filter.value.from_value > datetime.datetime.min.replace(
                tzinfo=datetime.timezone.utc).timestamp():
            return TurnoversFromTransactionsPrototype.calculate(
                self._store_transaction_storage.get_filtered(filters),
                grouping
            )

        cached_turnovers = self._get_cached_turnovers(filters, grouping, blocking_date)
        time_filter.value.from_value = blocking_date
        transactions = self._store_transaction_storage.get_filtered(filters)
        new_turnovers = TurnoversFromTransactionsPrototype().calculate(transactions, grouping)

        return TurnoversFromTransactionsPrototype.merge(cached_turnovers, new_turnovers)

    def _get_cached_turnovers(self, filters: list[Filter], grouping: list[str], blocking_date: datetime.datetime) \
            -> list[StoreTurnover]:

        turnovers = self._turnover_storage.get(blocking_date.timestamp())

        filters = deepcopy(filters)

        if turnovers is None or grouping != StoreTurnover.default_grouping():
            time_filter = FilterUtils.find_filter(filters, 'time', FilterType.BETWEEN)
            time_filter.value.from_value = datetime.datetime.min
            time_filter.value.to_value = blocking_date
            self._turnover_storage.clear()

            transactions = self._store_transaction_storage.get_filtered(filters)
            turnovers = TurnoversFromTransactionsPrototype().calculate(transactions, grouping)
            self._turnover_storage.update(blocking_date.timestamp(), turnovers)

        filters = FilterUtils.remove_filter(filters, 'time', FilterType.BETWEEN)
        turnovers = ListFilterer.apply_filters(turnovers, filters, value_to_filter='group')

        return turnovers
