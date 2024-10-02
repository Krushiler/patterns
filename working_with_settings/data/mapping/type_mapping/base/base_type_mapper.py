from abc import ABC, abstractmethod
from typing import TypeVar, Generic

MODEL = TypeVar('MODEL')


class BaseTypeMapper(ABC, Generic[MODEL]):

    @abstractmethod
    def from_model(self, obj):
        pass

    @abstractmethod
    def to_model(self, data) -> MODEL:
        pass
