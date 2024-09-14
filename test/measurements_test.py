from copy import deepcopy

import pytest

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


def test_measurements_add():
    meter = MeasurementUnit(name='m', convertion_ratio=1)
    kilometer = MeasurementUnit(name='km', convertion_ratio=1000)

    v1 = MeasuredValue(value=2000, unit=meter)
    v2 = MeasuredValue(value=1, unit=kilometer)

    res = v1 + v2

    assert res.value == 3000
    assert res.unit == meter


def test_measurements_sub():
    meter = MeasurementUnit(name='m', convertion_ratio=1)
    kilometer = MeasurementUnit(name='km', convertion_ratio=1000)

    v1 = MeasuredValue(value=2000, unit=meter)
    v2 = MeasuredValue(value=1, unit=kilometer)

    res = v1 - v2

    assert res.value == 1000
    assert res.unit == meter


def test_measurements_equals():
    meter = MeasurementUnit(name='m', convertion_ratio=1)
    kilometer = MeasurementUnit(name='km', convertion_ratio=1000)

    v1 = MeasuredValue(value=1000, unit=meter)
    v2 = MeasuredValue(value=1, unit=kilometer)

    assert v1 == v2
    assert meter != ''


def test_measurements_name_invalid_type():
    with pytest.raises(InvalidTypeException):
        MeasurementUnit(name=100, convertion_ratio=1)


def test_measurements_convertion_invalid_type():
    with pytest.raises(InvalidTypeException):
        MeasurementUnit(name='m', convertion_ratio='error')


def test_measurement_value_validation():
    with pytest.raises(InvalidTypeException):
        MeasuredValue(value='error', unit=MeasurementUnit(name='m', convertion_ratio=1))

    with pytest.raises(InvalidTypeException):
        MeasuredValue(value=1, unit='error')

    m = MeasuredValue(value=1, unit=MeasurementUnit(name='m', convertion_ratio=1))

    with pytest.raises(InvalidTypeException):
        m + ''

    with pytest.raises(InvalidTypeException):
        m - ''

    assert m != ''


def test_measurement_unit_equals():
    n1 = MeasurementUnit()
    n1.name = 'Test'

    n2 = MeasurementUnit()
    n2.name = 'Test'

    assert n1 == n2

    n2 = deepcopy(n1)
    n2.name = 'Test2'

    assert n1 != n2
