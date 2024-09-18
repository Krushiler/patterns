from working_with_settings.application.settings.settings_manager import SettingsManager
from working_with_settings.application.start.start_manager import StartManager
from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.factory.recipe.milk_pancakes_recipe_factory import \
    MilkPancakesRecipeFactory
from working_with_settings.data.factory.recipe.waffles_recipe_factory import WafflesRecipeFactory
from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.data.repository.recipe_repository import RecipeRepository
from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.di.di_utils import lazy


class Di:
    @lazy
    def get_settings_manager(self) -> SettingsManager:
        return SettingsManager(self.get_settings_repository())

    @lazy
    def get_start_manager(self) -> StartManager:
        return StartManager(self.get_recipe_repository())

    @lazy
    def get_settings_repository(self) -> SettingsRepository:
        return SettingsRepository()

    @lazy
    def get_recipe_repository(self) -> RecipeRepository:
        return RecipeRepository(self.get_recipe_storage(),
                                [self.get_milk_pancakes_recipe_factory(), self.get_waffles_recipe_factory()])

    @lazy
    def get_recipe_storage(self) -> RecipeStorage:
        return RecipeStorage()

    @lazy
    def get_start_nomenclature_factory(self) -> StartNomenclatureFactory:
        return StartNomenclatureFactory(self.get_measurement_units_factory())

    @lazy
    def get_measurement_units_factory(self) -> MeasurementUnitsFactory:
        return MeasurementUnitsFactory()

    @lazy
    def get_milk_pancakes_recipe_factory(self) -> MilkPancakesRecipeFactory:
        return MilkPancakesRecipeFactory(self.get_start_nomenclature_factory(), self.get_measurement_units_factory())

    @lazy
    def get_waffles_recipe_factory(self) -> MilkPancakesRecipeFactory:
        return WafflesRecipeFactory(self.get_start_nomenclature_factory(), self.get_measurement_units_factory())
