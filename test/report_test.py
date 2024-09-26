import pytest

from working_with_settings.domain.model.report.report_format import ReportFormat


@pytest.fixture
def report_factory(inject):
    return inject.get_report_factory()


@pytest.mark.parametrize('report_format', [ReportFormat.CSV, ReportFormat.MARKDOWN, ReportFormat.JSON, ReportFormat.XML,
                                           ReportFormat.RTF])
def test_report_nomenclature(inject, report_format, settings):
    generator = inject.get_start_nomenclature_factory()

    data = [generator.wheat_flour(), generator.milk(), generator.egg(), generator.sugar(), generator.baking_powder()]
    res = inject.get_report_factory().create(report_format, settings).create(data)

    with open(f'reports/report.{report_format.name.lower()}', 'w', encoding='utf-8') as file:
        file.write(res)


def test_report_default(inject, settings):
    generator = inject.get_start_nomenclature_factory()

    data = [generator.wheat_flour(), generator.milk(), generator.egg(), generator.sugar(), generator.baking_powder()]
    res = inject.get_report_factory().create_default(settings).create(data)

    with open(f'reports/report_default.{settings.default_report_format.name.lower()}', 'w', encoding='utf-8') as file:
        file.write(res)
