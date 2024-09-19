import pytest

from working_with_settings.di.di import Di
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidUnitException
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.recipe.ingredient import Ingredient
from working_with_settings.domain.model.recipe.recipe import Recipe


def test_start_recipes_not_added_with_existing_recipes(inject: Di):
    start_storage = inject.get_start_recipes_storage()
    storage = inject.get_recipe_storage()

    storage.create(start_storage.get_recipes()[0])

    inject.get_start_manager().init()
    recipe_repository = inject.get_recipe_repository()

    assert len(recipe_repository.get_recipes()) == 1


def test_start_recipes_added_with_existing_recipes(inject: Di):

    inject.get_start_manager().init()
    recipe_repository = inject.get_recipe_repository()

    print(recipe_repository.get_recipes())

    assert len(recipe_repository.get_recipes()) == 2


def test_recipe_validation(inject: Di):
    with pytest.raises(InvalidTypeException):
        Recipe(ingredients=[''])

    with pytest.raises(InvalidTypeException):
        Recipe(cooking_steps=[1])

    with pytest.raises(InvalidTypeException):
        Recipe(cooking_time=1)


def test_ingredient_same_unit(inject: Di):
    u1 = MeasurementUnit(name='a', convertion_ratio=1)
    u2 = MeasurementUnit(name='b', convertion_ratio=1, base_unit=u1)
    u3 = MeasurementUnit(name='c', convertion_ratio=1)

    n = Nomenclature(name='m', unit=u1)

    Ingredient(nomenclature=n, measured_amount=MeasuredValue(value=1, unit=u2))

    with pytest.raises(InvalidUnitException):
        Ingredient(nomenclature=n, measured_amount=MeasuredValue(value=1, unit=u3))
