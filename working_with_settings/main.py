import json
import os


class Settings:
    # В проде такие вещи должны быть immutable
    # Если очень хочется, cделать Builder
    def __init__(self):
        self._organization_name = ''
        self._inn = ''
        self._director_name = ''

    @property
    def organization_name(self):
        return self._organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('organization_name must be str')
        self._organization_name = value

    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise TypeError('inn must be str')
        if not value.isdigit():
            raise ValueError('inn must be digits')
        if len(value) != 12:
            raise ValueError('inn must be 12 chars long')
        self._inn = value

    @property
    def director_name(self):
        return self._director_name

    @director_name.setter
    def director_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('director_name must be str')
        self._director_name = value

    def __str__(self):
        return f'organization_name: {self.organization_name}, inn: {self.inn}, director_name: {self.director_name}'


class SettingMapper:
    @staticmethod
    def from_json(json: dict) -> Settings:
        # Это плохое решение, т.к. лучше мэппить явно, чтобы модель не зависела от json'а.
        # Здесь же мы теряем конроль над мэппингом.
        # Например, если мы захотим string или timestamp из json превратить в DateTime в бизнес-модели.
        if not isinstance(json, dict):
            raise TypeError('Dict must be provided')
        settings = Settings()
        for field in dir(settings):
            if field in json:
                setattr(settings, field, json[field])
        return settings


class SettingsLoader:
    # Репозиторий

    @staticmethod
    def load_from_file(file_name: str) -> Settings:
        if not isinstance(file_name, str):
            raise TypeError('file_name must be str')

        full_name = os.path.abspath(file_name)

        with open(full_name, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            settings = SettingMapper.from_json(json_data)

        return settings


class SettingsManager:
    # По сути выполняет роль вьюмодели

    _file_name = ''
    _settings = Settings()

    @staticmethod
    def _default_settings() -> Settings:
        settings = Settings()
        settings.organization_name = 'Рога и копыта'
        settings.inn = '123456789016'
        settings.director_name = 'Иванов Иван Иванович'
        return settings

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return getattr(cls, '_instance')

    def open(self, file_name: str) -> bool:
        try:
            self._settings = SettingsLoader.load_from_file(file_name)
            if file_name != '':
                self._file_name = file_name
            return True
        except Exception as e:
            print(f'Unable to load from file {file_name}', e, sep='\n')
            self._settings = self._default_settings()
            return False

    def settings(self):
        return self._settings


sm1 = SettingsManager()

# Windows absolute path expample
# C:\\Users\\User\\Downloads\\settings_success.json
sm1.open('data/settings_success.json')

sm2 = SettingsManager()

print(sm1.settings())
print(sm2.settings())
