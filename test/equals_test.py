from copy import deepcopy

from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


def test_nomenclature_equals():
    n1 = Nomenclature()
    n1.name = 'Test'

    n2 = Nomenclature()
    n2.name = 'Test'

    assert n1 != n2

    n2 = deepcopy(n1)
    n2.name = 'Test2'

    assert n1 == n2


def test_measurement_unit_equals():
    n1 = MeasurementUnit()
    n1.name = 'Test'

    n2 = MeasurementUnit()
    n2.name = 'Test'

    assert n1 == n2

    n2 = deepcopy(n1)
    n2.name = 'Test2'

    assert n1 != n2
