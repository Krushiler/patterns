from typing import TypeVar

from working_with_settings.util.stream.base.base_stream import BaseStream
from working_with_settings.util.stream.stream_subscription import StreamSubscription

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

    @classmethod
    def seeded(cls, value: T):
        stream = cls()
        stream.emit(value)
        return stream

    @property
    def value(self) -> T | None:
        return self._value

    def emit(self, value: T):
        for subscription in self._subscriptions:
            subscription.call(value)

    def _subscribe_internal(self, subscription: StreamSubscription):
        subscription.call(self.value)
