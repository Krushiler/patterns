from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.util.stream.base.base_observable import BaseObservable
from working_with_settings.util.stream.streams import EventStream

K = TypeVar('K')
V = TypeVar('V', covariant=True, bound=BaseModel)


class BaseStorage(Generic[K, V], ABC):
    _deletions: EventStream[str] = EventStream()
    _updates: EventStream[V] = EventStream()

    @property
    def deletions(self) -> BaseObservable[str]:
        return self._deletions.as_read_only()

    @property
    def updates(self) -> BaseObservable[str]:
        return self._updates.as_read_only()

    @abstractmethod
    def contains_key(self, key: K) -> bool:
        pass

    @abstractmethod
    def get(self, key: K) -> V | None:
        pass

    @abstractmethod
    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        pass

    @abstractmethod
    def create(self, value: V):
        pass

    def update(self, key: K, value: V):
        self._update_internal(key, value)
        self._updates.emit(value)

    @abstractmethod
    def _update_internal(self, key: K, value: V):
        pass

    def delete(self, key: K):
        self._delete_internal(key)
        self._deletions.emit(key)

    @abstractmethod
    def _delete_internal(self, key: K):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_filtered(self, filters: list[Filter]) -> list[V]:
        pass
