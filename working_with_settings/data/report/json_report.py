import json

from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class JsonReport(BaseReport):

    def create_from_serialized(self, obj: dict, original_obj: list[BaseModel]) -> str:
        return json.dumps(obj, indent=4, sort_keys=True, default=str, ensure_ascii=False)

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.JSON
