from abc import ABC

from working_with_settings.data.storage.base.base_storage import BaseStorage, K, V
from working_with_settings.data.storage.filterer.list_filterer import ListFilterer
from working_with_settings.domain.model.filter.filter import Filter


class BaseMemoryStorage(BaseStorage[K, V], ABC):

    def __init__(self):
        self._data = {}

    def contains_key(self, key: K) -> bool:
        return key in self._data

    def get(self, key: K) -> V | None:
        return self._data.get(key)

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        values = list(self._data.values())
        if limit is not None:
            values = values[offset:offset + limit]
        else:
            values = values[offset:]
        return values

    def create(self, value: V):
        self._data[value.id] = value

    def _update_internal(self, key: K, value: V):
        self._data[key] = value

    def _delete_internal(self, key: K):
        del self._data[key]

    def clear(self):
        self._data.clear()

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def get_filtered(self, filters: list[Filter]) -> list[V]:
        return ListFilterer.apply_filters(self._data.values(), filters)
