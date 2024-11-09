from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable

from working_with_settings.util.stream.stream_subscription import StreamSubscription

T = TypeVar('T')


class BaseObservable(ABC, Generic[T]):
    @abstractmethod
    def subscribe(self, call: Callable[[T], None]):
        pass

    @abstractmethod
    def unsubscribe(self, subscription: StreamSubscription):
        pass
