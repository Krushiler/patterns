from working_with_settings.util.logging.log import Log, LogLevel
from working_with_settings.util.stream.base.base_observable import BaseObservable
from working_with_settings.util.stream.streams import EventStream


class Logger:
    _log_events: EventStream[Log] = EventStream()

    @staticmethod
    def watch_logs() -> BaseObservable[Log]:
        return Logger._log_events.as_read_only()

    @staticmethod
    def log(level: LogLevel, tag: str, message: str):
        log = Log(level, tag, message)
        Logger._log_events.emit(log)

    @staticmethod
    def debug(tag: str, message: str):
        Logger.log(LogLevel.DEBUG, tag, message)

    @staticmethod
    def info(tag: str, message: str):
        Logger.log(LogLevel.INFO, tag, message)

    @staticmethod
    def error(tag: str, message: str):
        Logger.log(LogLevel.ERROR, tag, message)
