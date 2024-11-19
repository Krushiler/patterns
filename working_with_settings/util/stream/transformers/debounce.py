import datetime

from working_with_settings.util.stream.base.base_observable import BaseObservable, T
from working_with_settings.util.stream.streams import EventStream


class Debounce(EventStream[T]):
    _debounce_time: datetime.timedelta
    _stream: BaseObservable
    _last_write: datetime.datetime

    _ticker: BaseObservable

    def __init__(self, debounce_time: datetime.timedelta, stream: BaseObservable):
        super().__init__()
        self._stream = stream
        self._debounce_time = debounce_time
        self._last_write = datetime.datetime.fromtimestamp(0)

        stream.subscribe(self._listen_stream)

    def _listen_stream(self, data: T):
        delta = datetime.datetime.now() - self._last_write

        if delta >= self._debounce_time:
            self.emit(data)
            self._last_write = datetime.datetime.now()
