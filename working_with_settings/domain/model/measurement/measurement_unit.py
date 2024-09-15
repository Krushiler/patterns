from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel


class MeasurementUnit(BaseModel):
    def __init__(self, name: str = '', convertion_ratio: float = 1.0):
        super().__init__()
        self._name = ''
        self._convertion_ratio = 1
        self.name = name
        self.convertion_ratio = convertion_ratio

    @property
    def convertion_ratio(self) -> float:
        return self._convertion_ratio

    @convertion_ratio.setter
    def convertion_ratio(self, value):
        try:
            value = float(value)
            self._convertion_ratio = value
        except:
            raise InvalidTypeException(float, type(value))

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
