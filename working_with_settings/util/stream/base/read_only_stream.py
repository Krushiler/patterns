from typing import TypeVar, Callable

from working_with_settings.util.stream.base.base_observable import BaseObservable
from working_with_settings.util.stream.stream_subscription import StreamSubscription

T = TypeVar('T')


class ReadOnlyStream(BaseObservable[T]):
    def __init__(self, stream: BaseObservable[T]):
        self._stream = stream

    def subscribe(self, call: Callable[[T], None]):
        self._stream.subscribe(call)

    def unsubscribe(self, subscription: StreamSubscription):
        self._stream.unsubscribe(subscription)
