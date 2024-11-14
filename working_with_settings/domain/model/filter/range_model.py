import datetime

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException


class RangeModel:
    # consumes any comparable type because lack of generics

    _from_value: datetime.datetime | float | int
    _to_value: datetime.datetime | float | int

    def __init__(self, from_value, to_value):
        self.from_value = from_value
        self.to_value = to_value

    @staticmethod
    def _map_value(value):
        if isinstance(value, datetime.datetime):
            return value.timestamp()
        return value

    @property
    def from_value(self) -> float:
        return RangeModel._map_value(self._from_value)

    @from_value.setter
    def from_value(self, value):
        if not isinstance(value, (datetime.datetime, float, int)):
            raise InvalidTypeException((datetime.datetime, float, int), type(value))
        self._from_value = value

    @property
    def to_value(self) -> float:
        return RangeModel._map_value(self._to_value)

    @to_value.setter
    def to_value(self, value):
        if not isinstance(value, (datetime.datetime, float, int)):
            raise InvalidTypeException((datetime.datetime, float, int), type(value))
        self._to_value = value
