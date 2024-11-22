import json
import os

from working_with_settings.data.mapping.settings_mapper import SettingsMapper
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.organization.settings import Settings
from working_with_settings.util.logging.logger import Logger


class SettingsRepository:
    @staticmethod
    def load_from_file(file_name: str) -> Settings:
        if not isinstance(file_name, str):
            raise InvalidTypeException(str, type(file_name))

        full_name = os.path.abspath(file_name)

        with open(full_name, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            settings = SettingsMapper.from_json(json_data)

        return settings

    @staticmethod
    def save_to_file(file_name: str, settings: Settings) -> bool:
        if not isinstance(file_name, str):
            raise InvalidTypeException(str, type(file_name))
        if not isinstance(settings, Settings):
            raise InvalidTypeException(Settings, type(settings))

        try:
            full_name = os.path.abspath(file_name)
            if not os.path.exists(full_name):
                os.makedirs(os.path.dirname(full_name), exist_ok=True)
            with open(full_name, 'w', encoding='utf-8') as f:
                json_data = SettingsMapper.to_json(settings)
                json.dump(json_data, f, ensure_ascii=False, indent=4)

            return True
        except:
            Logger.error(SettingsRepository.__class__.__name__, 'Unable to save settings to file')
            return False
