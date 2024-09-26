import csv
import io

from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class CsvReport(BaseReport):

    def create_from_serialized(self, obj: dict, original_obj: list[BaseModel]) -> str:
        flat_dicts = [self._flatten_dict(item) for item in obj]
        fieldnames = flat_dicts[0].keys()

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()

        for flat_dict in flat_dicts:
            writer.writerow(flat_dict)

        return output.getvalue()

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.CSV
