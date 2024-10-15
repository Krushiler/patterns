import enum

from working_with_settings.domain.model.base.enum_meta import EnumMeta


class FilterType(enum.Enum, metaclass=EnumMeta):
    EQUALS = 0
    LIKE = 1
