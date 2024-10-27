import pytest

from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit
from working_with_settings.domain.prototype.common.grouping_prototype import GroupingPrototype


@pytest.fixture
def data() -> list[MeasuredValue]:
    return [
        MeasuredValue(1, MeasurementUnit('гр', 1000)),
        MeasuredValue(10, MeasurementUnit('гр', 1000)),
        MeasuredValue(1, MeasurementUnit('л', 1)),
    ]


def test_nested_grouping(data):
    res = list(GroupingPrototype.group(data, ['unit.name']))

    assert len(res) == 2


def test_multiple_parameters_grouping(data):
    res = list(GroupingPrototype.group(data, ['value', 'unit.name']))

    assert len(res) == 3
