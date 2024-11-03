from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


class MeasuredValue(BaseModel):
    _value: float = 0
    _unit: MeasurementUnit = None

    def __init__(self, value: float = None, unit: MeasurementUnit = None):
        super().__init__()
        self.value = value
        self.unit = unit

    def to_root(self) -> 'MeasuredValue':
        if self.unit.base_unit is None:
            return self
        return MeasuredValue(self.converted_value, self.unit.base_unit).to_root()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            value = float(value)
            self._value = value
        except:
            raise InvalidTypeException(float, type(value))

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if not isinstance(value, MeasurementUnit):
            raise InvalidTypeException(MeasurementUnit, type(value))
        self._unit = value

    @property
    def converted_value(self):
        return self.value * self.unit.convertion_ratio

    def __add__(self, other):
        if not isinstance(other, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(other))
        return MeasuredValue((self.converted_value + other.converted_value) / self.unit.convertion_ratio, self.unit)

    def __sub__(self, other):
        if not isinstance(other, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(other))
        return MeasuredValue((self.converted_value - other.converted_value) / self.unit.convertion_ratio, self.unit)

    def equals(self, other):
        if not isinstance(other, MeasuredValue):
            return False
        return self.converted_value == other.converted_value
