from typing import TypeVar

from working_with_settings.data.storage.filterer.filter_type_processor import LikeFilterTypeProcessor, \
    EqualsFilterTypeProcessor
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType

T = TypeVar('T')


class ListFilterer:
    __filterers_map = {
        FilterType.LIKE: LikeFilterTypeProcessor(),
        FilterType.EQUALS: EqualsFilterTypeProcessor()
    }

    @staticmethod
    def apply_filters(items: list[T], filters: list[Filter]) -> list[T]:
        return [item for item in items if
                all(ListFilterer.__filterers_map[filter.filter_type].process(item, filter) for filter in filters)]
