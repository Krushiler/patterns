from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidUnitException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class Ingredient(BaseModel):
    _nomenclature: Nomenclature = None
    _measured_amount: MeasuredValue = None

    def __init__(self, nomenclature: Nomenclature = None, measured_amount: MeasuredValue = None):
        super().__init__()

        self.nomenclature = nomenclature
        self.measured_amount = measured_amount

    @property
    def nomenclature(self) -> Nomenclature:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise InvalidTypeException(Nomenclature, type(value))
        self._nomenclature = value

    @property
    def measured_amount(self) -> MeasuredValue:
        return self._measured_amount

    @measured_amount.setter
    def measured_amount(self, value: MeasuredValue):
        if not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        if not value.unit.has_same_base(self.nomenclature.unit):
            raise InvalidUnitException(self.nomenclature.unit, value.unit)
        self._measured_amount = value
