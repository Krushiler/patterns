from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType
from working_with_settings.domain.model.store.store_turnover import StoreTurnover
from working_with_settings.domain.process.base.base_process import BaseProcess
from itertools import groupby


class TurnoversFromTransactionsProcess(BaseProcess[list[StoreTransaction], list[StoreTurnover]]):
    def calculate(self, inp: list[StoreTransaction]) -> list[StoreTurnover]:
        groups = groupby(inp, lambda x: (x.store, x.nomenclature))

        return [self._calculate_group(group) for group in groups]

    def _calculate_group(self, group) -> StoreTurnover:
        key, transactions = group
        transactions = list(transactions)

        value = MeasuredValue(0.0, key[1].unit)

        for transaction in transactions:
            match transaction.transaction_type:
                case StoreTransactionType.INCOME:
                    value = value + transaction.amount
                case StoreTransactionType.EXPENSE:
                    value = value - transaction.amount

        return StoreTurnover(key[0], value, key[1])
