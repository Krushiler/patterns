from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.recipe_repository import RecipeRepository
from working_with_settings.data.storage.measurement_unit_storage import MeasurementUnitStorage


class StartManager(BaseManager[BaseState]):
    def __init__(self, recipe_repository: RecipeRepository, nomenclature_repository: NomenclatureRepository,
                 measurement_unit_storage: MeasurementUnitStorage,
                 measurement_units_factory: MeasurementUnitsFactory):
        super().__init__(BaseState())

        self._recipe_repository = recipe_repository
        self._nomenclature_repository = nomenclature_repository
        self._measurement_unit_storage = measurement_unit_storage
        self._measurement_units_factory = measurement_units_factory

    def init(self):
        self._recipe_repository.init_start_recipes()
        self._nomenclature_repository.init_start_nomenclature()
        for unit in self._measurement_units_factory.get_units():
            self._measurement_unit_storage.create(unit)
