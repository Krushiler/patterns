from working_with_settings.domain.model.settings import Settings


class SettingsMapper:
    @staticmethod
    def from_json(json: dict) -> Settings:
        if not isinstance(json, dict):
            raise TypeError('Dict must be provided')
        settings = Settings()
        settings.organization_name = json['organization_name']
        settings.inn = json['inn']
        settings.director_name = json['director_name']
        return settings
