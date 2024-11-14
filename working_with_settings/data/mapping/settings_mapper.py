import datetime

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.organization.settings import Settings


class SettingsMapper:
    @staticmethod
    def from_json(json: dict) -> Settings:
        if not isinstance(json, dict):
            raise InvalidTypeException(dict, type(json))
        settings = Settings(
            ownership_form=json['ownership_form'],
            inn=json['inn'],
            bic=json['bic'],
            account=json['account'],
            blocking_date=datetime.datetime.fromtimestamp(json['blocking_date']),
            first_start=json['first_start'],
        )
        return settings

    @staticmethod
    def to_json(settings: Settings) -> dict:
        return {
            'ownership_form': settings.ownership_form,
            'inn': settings.inn,
            'bic': settings.bic,
            'account': settings.account,
            'blocking_date': settings.blocking_date.timestamp(),
            'first_start': settings.first_start,
        }
