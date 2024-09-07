import json
import os

from working_with_settings.data.mapping.settings_mapper import SettingsMapper
from working_with_settings.domain.model.settings import Settings


class SettingsRepository:
    @staticmethod
    def load_from_file(file_name: str) -> Settings:
        if not isinstance(file_name, str):
            raise TypeError('file_name must be str')

        full_name = os.path.abspath(file_name)

        with open(full_name, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            settings = SettingsMapper.from_json(json_data)

        return settings
