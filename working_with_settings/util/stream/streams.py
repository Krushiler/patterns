from typing import TypeVar

from working_with_settings.util.stream.base.base_observable import StreamSubscription
from working_with_settings.util.stream.base.base_stream import BaseStream

T = TypeVar('T')


class EventStream(BaseStream[T]):
    """
    Горячий поток
    """

    def emit(self, value: T):
        for subscription in self._subscriptions:
            subscription.call(value)


class ValueStream(BaseStream[T]):
    """
    Холодный поток
    """
    _value: T | None = None
    _has_data = False

    @classmethod
    def seeded(cls, value: T):
        stream = cls()
        stream._value = value
        stream._has_data = True
        return stream

    @property
    def value(self) -> T | None:
        return self._value

    def emit(self, value: T):
        self._has_data = True
        for subscription in self._subscriptions:
            subscription.call(value)

    def _subscribe_internal(self, subscription: StreamSubscription):
        if self._has_data:
            subscription.call(self.value)
