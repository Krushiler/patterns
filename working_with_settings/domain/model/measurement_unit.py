from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel


class MeasurementUnit(BaseModel):
    def __init__(self):
        super().__init__()
        self._name = ''

    @property
    def name(self):
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
