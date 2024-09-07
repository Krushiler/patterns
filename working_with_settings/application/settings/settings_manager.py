from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.domain.model.settings import Settings


class SettingsManager:

    def __init__(self, settings_repository: SettingsRepository):
        self._settings_repository = settings_repository
        self._file_name = ''
        self._settings = Settings()

    @staticmethod
    def _default_settings() -> Settings:
        settings = Settings()
        settings.organization_name = 'Рога и копыта'
        settings.inn = '123456789016'
        settings.director_name = 'Иванов Иван Иванович'
        return settings

    def open(self, file_name: str) -> bool:
        try:
            self._settings = self._settings_repository.load_from_file(file_name)
            if file_name != '':
                self._file_name = file_name
            return True
        except Exception as e:
            print(f'Unable to load from file {file_name}', e, sep='\n')
            self._settings = self._default_settings()
            return False

    def settings(self):
        return self._settings
