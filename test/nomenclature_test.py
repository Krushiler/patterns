from copy import deepcopy

import pytest

from working_with_settings.domain.model.organization.nomenclature_group import NomenclatureGroup
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException
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
    assert n1.nomenclature_group_id == n2.nomenclature_group_id
    assert n1.name != n2.name


def test_nomenclature_name_validation():
    with pytest.raises(InvalidTypeException):
        Nomenclature(nomenclature_group_id=1)

    with pytest.raises(InvalidTypeException):
        Nomenclature(name=1)

    with pytest.raises(InvalidLengthException):
        Nomenclature(name='Test' * 300)


def test_nomenclature_group_validation():
    with pytest.raises(InvalidTypeException):
        NomenclatureGroup(name=1)

    g = NomenclatureGroup(name='Test')

    assert g.name == 'Test'
