import datetime

from working_with_settings.data.mapping.type_mapping.base.base_type_mapper import BaseTypeMapper


class DatetimeMapper(BaseTypeMapper[datetime.datetime]):

    def from_model(self, obj: datetime.datetime) -> float:
        return obj.replace(tzinfo=datetime.timezone.utc).timestamp()

    def to_model(self, data: float) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(data)
