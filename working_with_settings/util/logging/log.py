from enum import Enum

from working_with_settings.domain.model.base.enum_meta import EnumMeta


class LogLevel(Enum, metaclass=EnumMeta):
    DEBUG = 0
    INFO = 1
    ERROR = 2


class Log:
    _level: LogLevel = None
    _tag: str = None
    _message: str = None

    def __init__(self, level: LogLevel, tag: str, message: str):
        self._level = level
        self._tag = tag
        self._message = message

    @property
    def level(self) -> LogLevel:
        return self._level

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def message(self) -> str:
        return self._message
