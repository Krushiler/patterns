from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.data.report.csv_report import CsvReport
from working_with_settings.data.report.json_report import JsonReport
from working_with_settings.data.report.markdown_report import MarkdownReport
from working_with_settings.data.report.rtf_report import RtfReport
from working_with_settings.data.report.xml_report import XmlReport
from working_with_settings.domain.exceptions.base.base_exception import ArgumentException
from working_with_settings.domain.model.report.report_format import ReportFormat


class ReportFactory:
    def __init__(self):
        self._report_map = {
            ReportFormat.CSV: CsvReport,
            ReportFormat.MARKDOWN: MarkdownReport,
            ReportFormat.JSON: JsonReport,
            ReportFormat.XML: XmlReport,
            ReportFormat.RTF: RtfReport
        }

    def create(self, report_format: ReportFormat) -> BaseReport:
        report = self._report_map[report_format]()

        if report is None:
            raise ArgumentException('Unknown report format: {}'.format(report_format))

        return report
