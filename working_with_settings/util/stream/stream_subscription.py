from typing import TypeVar, Generic, Callable

from working_with_settings.util.stream.streams import BaseStream

T = TypeVar('T')


class StreamSubscription(Generic[T]):
    def __init__(self, stream: BaseStream[T], call: Callable[[T], None]):
        self._stream = stream
        self._call = call

    def call(self, data: T):
        self._call(data)

    def close(self):
        self._stream.unsubscribe(self)
        self._stream = None
