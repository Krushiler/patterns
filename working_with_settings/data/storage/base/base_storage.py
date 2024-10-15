from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.filter.filter import Filter

K = TypeVar('K')
V = TypeVar('V', covariant=True, bound=BaseModel)


class BaseStorage(Generic[K, V], ABC):
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

    @abstractmethod
    def update(self, key: K, value: V):
        pass

    @abstractmethod
    def delete(self, key: K):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_filtered(self, filters: list[Filter]) -> list[V]:
        pass
