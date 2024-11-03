from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.store.store_transaction import StoreTransaction, StoreTransactionType
from working_with_settings.domain.model.store.store_turnover import StoreTurnover
from working_with_settings.domain.prototype.common.grouping_prototype import GroupingPrototype


class TurnoversFromTransactionsPrototype:
    @staticmethod
    def calculate(inp: list[StoreTransaction], grouping: list[str]) -> list[StoreTurnover]:
        groups = GroupingPrototype.group(inp, grouping)
        return [TurnoversFromTransactionsPrototype._calculate_group(group, grouping) for group in groups]

    @staticmethod
    def _calculate_group(group, grouping) -> StoreTurnover:
        key, transactions = group
        transactions = list(transactions)

        value = MeasuredValue(0.0, transactions[0].nomenclature.unit)

        for transaction in transactions:
            match transaction.transaction_type:
                case StoreTransactionType.INCOME:
                    value = value + transaction.amount
                case StoreTransactionType.EXPENSE:
                    value = value - transaction.amount

        group_data = {}

        for i in range(len(key)):
            group_data[grouping[i]] = key[i]

        return StoreTurnover(turnover=value, group=group_data)

    @staticmethod
    def merge(t1: list[StoreTurnover], t2: list[StoreTurnover]) -> list[StoreTurnover]:
        result = t2
        for t1_i in t1:
            found = False
            for t2_i in t2:
                if t1_i.group == t2_i.group:
                    t2_i.turnover = t1_i.turnover + t2_i.turnover
                    found = True
                    break
            if not found:
                result.append(t1_i)
        return result
