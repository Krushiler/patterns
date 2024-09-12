from working_with_settings.domain.model.organization.settings import Settings


class SettingsMapper:
    @staticmethod
    def from_json(json: dict) -> Settings:
        if not isinstance(json, dict):
            raise TypeError('Dict must be provided')
        settings = Settings(
            ownership_form=json['ownership_form'],
            inn=json['inn'],
            bic=json['bic'],
            account=json['account']
        )
        return settings
