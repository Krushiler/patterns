import json
import os

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.data.mapping.settings_mapper import SettingsMapper
from working_with_settings.domain.model.organization.settings import Settings


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
