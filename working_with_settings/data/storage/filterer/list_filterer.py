from typing import TypeVar

from working_with_settings.data.storage.filterer.filter_type_processor import LikeFilterTypeProcessor, \
    EqualsFilterTypeProcessor, BetweenFilterTypeProcessor
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType

T = TypeVar('T')


class ListFilterer:
    __filterers_map = {
        FilterType.LIKE: LikeFilterTypeProcessor(),
        FilterType.EQUALS: EqualsFilterTypeProcessor(),
        FilterType.BETWEEN: BetweenFilterTypeProcessor()
    }

    @staticmethod
    def apply_filters(items: list[T], filters: list[Filter], value_to_filter=None) -> list[T]:
        return [item for item in items if
                all(ListFilterer.__filterers_map[filter.filter_type].process(item, filter, value_to_filter) for filter
                    in filters)]
