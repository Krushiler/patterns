from typing import Generic, TypeVar

import reactivex as rx

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException

T = TypeVar('T')


class BaseManager(Generic[T]):

    def __init__(self, default_state: T):
        self._stream = rx.subject.BehaviorSubject(default_state)

    @property
    def stream(self):
        return self._stream.value

    @property
    def state(self) -> T:
        return self._stream

    @state.setter
    def state(self, value):
        if not isinstance(value, rx.Observable):
            raise InvalidTypeException(T, type(value))
        self._stream.on_next(value)
