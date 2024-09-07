from working_with_settings.application.settings.settings_manager import SettingsManager
from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.di.di_utils import singleton


class Di:
    @singleton
    def get_settings_manager(self) -> SettingsManager:
        return SettingsManager(self.get_settings_repository())

    @singleton
    def get_settings_repository(self) -> SettingsRepository:
        return SettingsRepository()
