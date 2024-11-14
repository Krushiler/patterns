from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class OsvNomenclatureReport(BaseModel):
    _nomenclature: Nomenclature
    _amount: MeasuredValue

    def __init__(self, nomenclature: Nomenclature = None, amount: MeasuredValue = None):
        super().__init__()

        self.nomenclature = nomenclature
        self.amount = amount

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
