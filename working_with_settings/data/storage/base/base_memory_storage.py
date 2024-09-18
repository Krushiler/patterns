from abc import ABC
from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')


class BaseMemoryStorage(Generic[K, V], ABC):

    def __init__(self):
        self._data = {}

    def contains_key(self, key: K) -> bool:
        return key in self._data

    def get(self, key: K) -> V | None:
        return self._data[key]

    def get_all(self) -> list[V]:
        return list(self._data.values())

    def set(self, key: K, value: V):
        self._data[key] = value

    def remove(self, key: K):
        del self._data[key]

    def clear(self):
        self._data.clear()
