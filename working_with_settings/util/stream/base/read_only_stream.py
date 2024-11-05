from typing import TypeVar

from working_with_settings.util.stream.base.base_observable import BaseObservable
from working_with_settings.util.stream.stream_subscription import StreamSubscription

T = TypeVar('T')


class ReadOnlyStream(BaseObservable[T]):
    def __init__(self, stream: BaseObservable[T]):
        self._stream = stream

    def subscribe(self, subscription: StreamSubscription):
        self._stream.subscribe(subscription)

    def unsubscribe(self, subscription: StreamSubscription):
        self._stream.unsubscribe(subscription)
