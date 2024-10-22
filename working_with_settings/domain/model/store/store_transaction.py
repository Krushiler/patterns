import datetime
from enum import Enum

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.base.enum_meta import EnumMeta
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.store import Store


class StoreTransactionType(Enum, metaclass=EnumMeta):
    INCOME = 1
    EXPENSE = 2


class StoreTransaction(BaseModel):
    _store: Store = None
    _nomenclature: Nomenclature = None
    _amount: MeasuredValue = None
    _transaction_type: StoreTransactionType = None
    _time: datetime.datetime = None

    def __init__(self, store: Store = None, nomenclature: Nomenclature = None, amount: MeasuredValue = None,
                 transaction_type: StoreTransactionType = None, time: datetime.datetime = None):
        super().__init__()

        self.store = store
        self.nomenclature = nomenclature
        self.amount = amount
        self.transaction_type = transaction_type
        self.time = time

    @property
    def store(self) -> Store:
        return self._store

    @store.setter
    def store(self, value: Store):
        if not isinstance(value, Store):
            raise InvalidTypeException(Store, type(value))
        self._store = value

    @property
    def nomenclature(self) -> Nomenclature:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise InvalidTypeException(Nomenclature, type(value))
        self._nomenclature = value

    @property
    def amount(self) -> MeasuredValue:
        return self._amount

    @amount.setter
    def amount(self, value: MeasuredValue):
        if not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        self._amount = value

    @property
    def transaction_type(self) -> StoreTransactionType:
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value: StoreTransactionType):
        if not isinstance(value, StoreTransactionType):
            raise InvalidTypeException(StoreTransactionType, type(value))
        self._transaction_type = value

    @property
    def time(self) -> datetime.datetime:
        return self._time

    @time.setter
    def time(self, value: datetime.datetime):
        if not isinstance(value, datetime.datetime):
            raise InvalidTypeException(datetime.datetime, type(value))
        self._time = value
