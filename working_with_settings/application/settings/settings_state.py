from copy import deepcopy

from working_with_settings.domain.model.settings import Settings


class SettingsState:

    def __init__(self, settings: Settings = None, error: Exception = None, file_name: str = ''):
        self._settings = settings
        self._error = None
        self._file_name = ''

    @property
    def file_name(self):
        return self._file_name

    @property
    def settings(self):
        return self._settings

    @property
    def error(self):
        return self._error

    def with_file_name(self, value):
        self._file_name = value
        return deepcopy(self)

    def with_error(self, value):
        self._error = value
        return deepcopy(self)

    def with_settings(self, value):
        self._settings = value
        return deepcopy(self)
