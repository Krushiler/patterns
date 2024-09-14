from typing import Generic, TypeVar

L = TypeVar('L')
R = TypeVar('R')


class Either(Generic[L, R]):
    @classmethod
    def with_left(cls, value):
        return cls(value, None)

    @classmethod
    def with_right(cls, value):
        return cls(None, value)

    def __init__(self, left: L, right: R):
        self._left = left
        self._right = right

    @property
    def is_left(self) -> bool:
        return self._left is not None

    @property
    def is_right(self) -> bool:
        return self._right is not None

    @property
    def left(self) -> L:
        return self._left

    @property
    def right(self) -> R:
        return self._right
