from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class Ingredient(BaseModel):
    def __init__(self, name: Nomenclature, amount: MeasuredValue):
        super().__init__()

        self._name = None
        self._amount = None
        self.name = name
        self.amount = amount

    @property
    def name(self) -> Nomenclature:
        return self._name

    @name.setter
    def name(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise InvalidTypeException(Nomenclature, type(value))
        self._name = value

    @property
    def amount(self) -> MeasuredValue:
        return self._amount

    @amount.setter
    def amount(self, value: MeasuredValue):
        if not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
