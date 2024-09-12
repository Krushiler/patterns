from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


class MeasuredValue:
    def __init__(self, value: float, unit: MeasurementUnit):
        self.value = value
        self.unit = unit

    @property
    def converted_value(self):
        return self.value * self.unit.convertion_ration

    def __add__(self, other):
        if not isinstance(other, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(other))
        return MeasuredValue((self.converted_value + other.converted_value) / self.unit.convertion_ration, self.unit)

    def __sub__(self, other):
        if not isinstance(other, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(other))
        return MeasuredValue((self.converted_value - other.converted_value) / self.unit.convertion_ration, self.unit)
