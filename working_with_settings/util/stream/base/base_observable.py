from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from working_with_settings.util.stream.stream_subscription import StreamSubscription

T = TypeVar('T')


class BaseObservable(ABC, Generic[T]):
    @abstractmethod
    def subscribe(self, subscription: StreamSubscription):
        pass

    @abstractmethod
    def unsubscribe(self, subscription: StreamSubscription):
        pass
