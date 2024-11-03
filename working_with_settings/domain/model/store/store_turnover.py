from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue


class StoreTurnover(BaseModel):
    _turnover: MeasuredValue = None
    _group: dict[str, object] = None

    def __init__(self, turnover: MeasuredValue, group: dict[str, object] = None):
        super().__init__()

        self.turnover = turnover
        self.group = group

    @property
    def turnover(self) -> MeasuredValue:
        return self._turnover

    @turnover.setter
    def turnover(self, value: MeasuredValue):
        if not isinstance(value, MeasuredValue):
            raise InvalidTypeException(MeasuredValue, type(value))
        self._turnover = value

    @property
    def group(self) -> dict[str, object]:
        return self._group

    @group.setter
    def group(self, value: dict[str, object]):
        if not isinstance(value, dict):
            raise InvalidTypeException(dict, type(value))
        self._group = value

    @staticmethod
    def default_grouping() -> list[str]:
        return ['nomenclature.id', 'store.id']
