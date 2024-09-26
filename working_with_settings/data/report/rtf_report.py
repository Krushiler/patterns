from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class RtfReport(BaseReport):

    def create_from_serialized(self, obj: list[dict], original_obj: list[BaseModel]) -> str:
        rtf_content = [
            r"{\rtf1\ansi\deff0",
            r"{\fonttbl{\f0\fswiss Helvetica;}}",
            r"\f0\fs24"
        ]

        class_name = original_obj[0].__class__.__name__

        for i, flat_dict in enumerate([self._flatten_dict(item) for item in obj], 1):
            rtf_content.append(f"\\b {class_name} {i}:\\b0 \\par")
            for key, value in flat_dict.items():
                rtf_content.append(f"\\b {key}:\\b0 {value} \\par")
            rtf_content.append("\\par")

        rtf_content.append("}")
        return ''.join(rtf_content)

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.RTF
