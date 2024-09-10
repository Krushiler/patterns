from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.settings.settings_state import SettingsState
from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.domain.model.settings import Settings


class SettingsManager(BaseManager[SettingsState]):

    def __init__(self, settings_repository: SettingsRepository):
        super().__init__(SettingsState())
        self._settings_repository = settings_repository

    @staticmethod
    def _default_settings() -> Settings:
        settings = Settings()
        settings.organization_name = 'Рога и копыта'
        settings.inn = '123456789016'
        settings.director_name = 'Иванов Иван Иванович'
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
