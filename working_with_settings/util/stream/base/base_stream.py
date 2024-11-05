from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from working_with_settings.util.stream.base.base_observable import BaseObservable
from working_with_settings.util.stream.base.read_only_stream import ReadOnlyStream
from working_with_settings.util.stream.stream_subscription import StreamSubscription

T = TypeVar('T')


class BaseStream(Generic[T], BaseObservable, ABC):
    _subscriptions: list[StreamSubscription] = []

    def as_read_only(self) -> ReadOnlyStream:
        return ReadOnlyStream(self)

    def subscribe(self, subscription: StreamSubscription):
        self._subscriptions.append(subscription)
        self._subscribe_internal(subscription)

    def unsubscribe(self, subscription: StreamSubscription):
        self._subscriptions.remove(subscription)

    @abstractmethod
    def emit(self, value: T):
        pass

    def _subscribe_internal(self, subscription: StreamSubscription):
        pass
