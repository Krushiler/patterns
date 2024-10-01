import typing
import builtins

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel

_unit_class = typing.ForwardRef('MeasurementUnit')


class MeasurementUnit(BaseModel):
    _name: str = ''
    _convertion_ratio: str = 1
    _base_unit: _unit_class = None

    def __init__(self, name: str = None, convertion_ratio: float = None, base_unit: _unit_class = None):
        super().__init__()

        self.name = name
        self.convertion_ratio = convertion_ratio
        self.base_unit = base_unit

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

    @property
    def base_unit(self) -> _unit_class:
        return self._base_unit

    @base_unit.setter
    def base_unit(self, value: _unit_class):
        if value is None:
            return
        if not isinstance(value, MeasurementUnit):
            raise InvalidTypeException(MeasurementUnit, type(value))
        self._base_unit = value

    def equals(self, other):
        if not isinstance(other, MeasurementUnit):
            return False
        return self.name == other.name

    def has_same_base(self, other):
        if not isinstance(other, MeasurementUnit):
            return False

        if self == other:
            return True

        other_base = other
        self_base = self

        while other_base.base_unit is not None:
            other_base = other_base.base_unit

        while self_base.base_unit is not None:
            self_base = self_base.base_unit

        return other_base == self_base


builtins.MeasurementUnit = MeasurementUnit
