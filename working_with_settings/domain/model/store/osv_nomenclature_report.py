from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class OsvNomenclatureReport(BaseModel):
    _nomenclature: Nomenclature
    _start_amount: MeasuredValue
    _end_amount: MeasuredValue

    def __init__(self,
                 nomenclature: Nomenclature = None,
                 start_amount: MeasuredValue = None,
                 end_amount: MeasuredValue = None
                 ):
        super().__init__()

        self.nomenclature = nomenclature
        self.start_amount = start_amount
        self.end_amount = end_amount

    @property
    def nomenclature(self) -> Nomenclature:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise InvalidTypeException(Nomenclature, type(value))
        self._nomenclature = value

    @property
    def start_amount(self) -> MeasuredValue | None:
        return self._start_amount

    @start_amount.setter
    def start_amount(self, value: MeasuredValue):
        if value is not None and not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        self._start_amount = value

    @property
    def end_amount(self) -> MeasuredValue | None:
        return self._end_amount

    @end_amount.setter
    def end_amount(self, value: MeasuredValue):
        if value is not None and not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        self._end_amount = value

    @property
    def diff_amount(self) -> MeasuredValue | None:
        if self.start_amount is None or self.end_amount is None:
            return None
        return self.end_amount - self.start_amount
