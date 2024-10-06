import datetime

from working_with_settings.data.mapping.type_mapping.base.base_type_mapper import BaseTypeMapper


class TimedeltaMapper(BaseTypeMapper[datetime.timedelta]):

    def from_model(self, obj: datetime.timedelta) -> float:
        return obj.total_seconds()

    def to_model(self, data: float) -> datetime.timedelta:
        return datetime.timedelta(seconds=data)
