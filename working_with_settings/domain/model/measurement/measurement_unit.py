from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel


class MeasurementUnit(BaseModel):
    def __init__(self, name: str = '', convertion_ratio: float = 1.0):
        super().__init__()
        self._name = ''
        self._convertion_ratio = 1
        self._measurement_type = ''
        self.name = name
        self.convertion_ratio = convertion_ratio

    @property
    def convertion_ration(self) -> float:
        return self._convertion_ratio

    @convertion_ration.setter
    def convertion_ration(self, value):
        if not isinstance(value, float):
            raise InvalidTypeException(float, type(value))
        self._convertion_ratio = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._name = value

    def equals(self, other):
        if not isinstance(other, MeasurementUnit):
            return False
        return self.name == other.name
