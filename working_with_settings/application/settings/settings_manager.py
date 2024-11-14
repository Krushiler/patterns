from datetime import datetime

from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.settings.settings_state import SettingsState
from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.domain.model.organization.settings import Settings


class SettingsManager(BaseManager[SettingsState]):
    def __init__(self, settings_repository: SettingsRepository):
        super().__init__(SettingsState(settings=self._default_settings()))
        self._settings_repository = settings_repository
        self.open('settings.json')

    def mark_as_loaded(self):
        self.state.settings.first_start = False
        self._settings_repository.save_to_file(self.state.file_name, self.state.settings)

    @staticmethod
    def _default_settings() -> Settings:
        settings = Settings(
            inn='123456789012',
            ownership_form='Ownership',
            bic='Ozwell E. Spencer',
            account='Ozwell E. Spencer',
            blocking_date=datetime.now(),
            first_start=True
        )
        return settings

    def open(self, file_name: str) -> bool:
        try:
            self.state = self.state.with_settings(self._settings_repository.load_from_file(file_name))
            if file_name != '':
                self.state = self.state.with_file_name(file_name)
            return True
        except Exception as e:
            print(f'Unable to load from file {file_name}', e, sep='\n')
            self.state = SettingsState(
                settings=self._default_settings(),
                error=e,
                file_name=file_name
            )
            return False

    def change_blocking_date(self, date: datetime):
        settings = self.state.settings
        settings.blocking_date = date
        self.state = self.state.with_settings(settings)
        self._settings_repository.save_to_file(self.state.file_name, settings)
