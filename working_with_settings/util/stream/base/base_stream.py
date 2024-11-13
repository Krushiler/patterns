from abc import abstractmethod, ABC
from typing import TypeVar, Callable

from working_with_settings.util.stream.base.base_observable import BaseObservable, StreamSubscription
from working_with_settings.util.stream.base.read_only_stream import ReadOnlyStream

T = TypeVar('T')


class BaseStream(BaseObservable[T], ABC):
    _subscriptions: list[StreamSubscription]

    def __init__(self):
        self._subscriptions = []

    def as_read_only(self) -> ReadOnlyStream:
        return ReadOnlyStream(self)

    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription:
        subscription = StreamSubscription(self, call)

        self._subscriptions.append(subscription)
        self._subscribe_internal(subscription)

        return subscription

    def unsubscribe(self, subscription: StreamSubscription):
        self._subscriptions.remove(subscription)

    @abstractmethod
    def emit(self, value: T):
        pass

    def _subscribe_internal(self, subscription: StreamSubscription):
        pass
