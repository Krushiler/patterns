from enum import Enum

from working_with_settings.domain.model.base.enum_meta import EnumMeta


class ReportFormat(Enum, metaclass=EnumMeta):
    CSV = 1
    MARKDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5
