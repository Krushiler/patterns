from abc import ABC, abstractmethod
from typing import TypeVar

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter import Filter

T = TypeVar('T', bound=BaseModel)


class FilterTypeProcessor(ABC):

    def process(self, item: T, filter: Filter) -> bool:
        item_dict = AbsoluteMapper.to_dict(item)

        keys_array = filter.key.split('.')

        inner_value = item_dict

        for key in keys_array:
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False

        return self._process_internal(str(inner_value).lower(), str(filter.value).lower())

    @abstractmethod
    def _process_internal(self, value: str, waited_value: str) -> bool:
        raise NotImplementedError()


class LikeFilterTypeProcessor(FilterTypeProcessor):

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return value.find(waited_value) != -1


class EqualsFilterTypeProcessor(FilterTypeProcessor):

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return value == waited_value
