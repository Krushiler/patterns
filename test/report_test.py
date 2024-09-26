import pytest

from working_with_settings.domain.model.report.report_format import ReportFormat


@pytest.fixture
def report_factory(inject):
    return inject.get_report_factory()


@pytest.mark.parametrize('f', [ReportFormat.CSV, ReportFormat.MARKDOWN, ReportFormat.JSON, ReportFormat.XML,
                               ReportFormat.RTF])
def test_report_nomenclature(inject, f):
    generator = inject.get_start_nomenclature_factory()
    data = [generator.wheat_flour(), generator.milk(), generator.egg(), generator.sugar(), generator.baking_powder()]
    res = inject.get_report_factory().create(f).create(data)

    with open(f'reports/report.{f.name.lower()}', 'w', encoding='utf-8') as file:
        file.write(res)
