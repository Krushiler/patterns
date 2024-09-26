from working_with_settings.data.report.base.base_report import BaseReport
from working_with_settings.domain.exceptions.base.base_exception import ArgumentException
from working_with_settings.domain.model.organization.settings import Settings
from working_with_settings.domain.model.report.report_format import ReportFormat


class ReportFactory:
    @staticmethod
    def _create(report_format: ReportFormat, report_map: dict) -> BaseReport:
        report = report_map[report_format]

        if report is None:
            raise ArgumentException('Unknown report format: {}'.format(report_format))

        return report()

    def create(self, report_format: ReportFormat, settings: Settings) -> BaseReport:
        return self._create(report_format, settings.report_map)

    def create_default(self, settings: Settings) -> BaseReport:
        return self._create(settings.default_report_format, settings.report_map)
