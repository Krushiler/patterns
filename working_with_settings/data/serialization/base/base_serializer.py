from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class BaseSerializer(ABC, Generic[T]):

    @abstractmethod
    def serialize(self, obj) -> T:
        pass

    @abstractmethod
    def deserialize(self, data, cls: type):
        pass
