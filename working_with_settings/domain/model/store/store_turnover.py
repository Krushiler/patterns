from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.store.store import Store


class StoreTurnover(BaseModel):
    _store: Store = None
    _turnover: MeasuredValue = None
    _nomenclature: Nomenclature = None

    def __init__(self, store: Store = None, turnover: MeasuredValue = None, nomenclature: Nomenclature = None):
        super().__init__()

        self.store = store
        self.turnover = turnover
        self.nomenclature = nomenclature

    @property
    def store(self) -> Store:
        return self._store

    @store.setter
    def store(self, value: Store):
        if not isinstance(value, Store):
            raise InvalidTypeException(Store, type(value))
        self._store = value

    @property
    def turnover(self) -> MeasuredValue:
        return self._turnover

    @turnover.setter
    def turnover(self, value: MeasuredValue):
        if not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        self._turnover = value

    @property
    def nomenclature(self) -> Nomenclature:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise InvalidTypeException(Nomenclature, type(value))
        self._nomenclature = value
