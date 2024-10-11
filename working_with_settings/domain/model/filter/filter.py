from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter_type import FilterType


class Filter(BaseModel):
    _key: str = str
    _value: str = str
    _filter_type: FilterType = FilterType

    def __init__(self, key: str, value: str, filter_type: FilterType):
        super().__init__()
        self._key = key
        self._value = value
        self._filter_type = filter_type

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def filter_type(self):
        return self._filter_type

    @key.setter
    def key(self, value):
        self._key = value

    @value.setter
    def value(self, value):
        self._value = value

    @filter_type.setter
    def filter_type(self, value):
        self._filter_type = value
