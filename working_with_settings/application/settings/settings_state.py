from copy import deepcopy

from working_with_settings.application.base.base_state import BaseState
from working_with_settings.domain.model.organization.settings import Settings


class SettingsState(BaseState):

    def __init__(self, settings: Settings = None, file_name: str = ''):
        super().__init__()
        self._settings = settings
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @property
    def settings(self):
        return self._settings

    def with_file_name(self, value: str):
        state = deepcopy(self)
        state._file_name = value
        return state

    def with_settings(self, value: Settings):
        state = deepcopy(self)
        state._settings = value
        return state
