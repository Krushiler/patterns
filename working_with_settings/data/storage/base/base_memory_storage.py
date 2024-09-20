from abc import ABC

from working_with_settings.data.storage.base.base_storage import BaseStorage, K, V


class BaseMemoryStorage(BaseStorage[K, V], ABC):

    def __init__(self):
        self._data = {}

    def contains_key(self, key: K) -> bool:
        return key in self._data

    def get(self, key: K) -> V | None:
        return self._data[key]

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        values = list(self._data.values())
        if limit is not None:
            values = values[offset:offset + limit]
        else:
            values = values[offset:]
        return values

    def create(self, value: V):
        self._data[value.id] = value

    def update(self, key: K, value: V):
        self._data[key] = value

    def delete(self, key: K):
        del self._data[key]

    def is_empty(self) -> bool:
        return len(self._data) == 0
