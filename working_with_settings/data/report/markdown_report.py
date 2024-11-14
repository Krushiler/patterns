from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.report.report_format import ReportFormat


class MarkdownReport(BaseReport):

    def create_from_serialized(self, obj: dict, original_obj: list[BaseModel]) -> str:
        markdown_lines = []
        flat_dicts = [self._flatten_dict(item) for item in obj]

        class_name = original_obj.__class__.__name__

        for i, flat_dict in enumerate(flat_dicts, 1):
            markdown_lines.append(f"### {class_name} {i}\n")
            for key, value in flat_dict.items():
                markdown_lines.append(f"**{key}**: {value}")
            markdown_lines.append("\n---\n")

        return "\n".join(markdown_lines)

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.MARKDOWN
