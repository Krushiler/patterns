from abc import ABC, abstractmethod
from typing import TypeVar

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.range_model import RangeModel

T = TypeVar('T', bound=BaseModel)


class FilterTypeProcessor(ABC):

    def process(self, item: T, filter: Filter, value_to_filter=None) -> bool:
        item_dict = AbsoluteMapper.to_dict(item)

        keys_array = filter.key.split('.')

        inner_value = item_dict

        if value_to_filter is not None:
            inner_value = inner_value.get(value_to_filter, None)
            if inner_value is None:
                return False

        return self._process_item(inner_value, filter, keys_array)

    def _process_item(self, inner_value: dict, filter: Filter, keys_array: list[str]) -> bool:
        key_idx = 0

        for key in keys_array:
            if isinstance(inner_value, list):
                return any([self._process_item(value, filter, keys_array[key_idx + 1:]) for value in inner_value])
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False
            key_idx += 1

        return self._process_internal(inner_value, filter.value)

    @abstractmethod
    def _process_internal(self, value: str, waited_value: str) -> bool:
        raise NotImplementedError()


class LikeFilterTypeProcessor(FilterTypeProcessor):

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return str(value).lower().find(str(waited_value).lower()) != -1


class EqualsFilterTypeProcessor(FilterTypeProcessor):

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return str(value).lower() == str(waited_value).lower()


class BetweenFilterTypeProcessor(FilterTypeProcessor):
    def _process_internal(self, value, waited_value: RangeModel) -> bool:
        return waited_value.from_value <= value < waited_value.to_value
