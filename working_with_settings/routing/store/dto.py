import datetime

from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter import Filter


class TransactionsRequestDto(BaseModel):
    _filters: list[Filter]
    _date_from: int
    _date_to: int

    @property
    def filters(self) -> list[Filter]:
        return self._filters

    @property
    def date_from(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self._date_from)

    @property
    def date_to(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self._date_to)

    @filters.setter
    def filters(self, value: list[Filter]):
        self._filters = value

    @date_from.setter
    def date_from(self, value: datetime.datetime):
        self._date_from = value

    @date_to.setter
    def date_to(self, value: datetime.datetime):
        self._date_to = value
