from working_with_settings.application.organization.nomenclature_manager import NomenclatureManager
from working_with_settings.application.settings.settings_manager import SettingsManager
from working_with_settings.application.start.start_manager import StartManager
from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.factory.report_factory import ReportFactory
from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.data.factory.start_recipes_factory import StartRecipesStorage
from working_with_settings.data.factory.start_store_factory import StartStoreFactory
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.recipe_repository import RecipeRepository
from working_with_settings.data.repository.settings_repository import SettingsRepository
from working_with_settings.data.repository.store_repository import StoreRepository
from working_with_settings.data.serialization.json_serializer import JsonSerializer
from working_with_settings.data.storage.measurement_unit_storage import MeasurementUnitStorage
from working_with_settings.data.storage.nomenclature_group_storage import NomenclatureGroupStorage
from working_with_settings.data.storage.nomenclature_storage import NomenclatureStorage
from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.data.storage.store_storage import StoreStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.data.storage.turnover_storage import TurnoverStorage
from working_with_settings.data.storage_finder.nomenclature_storage_finder import NomenclatureStorageFinder
from working_with_settings.di.di_utils import lazy


class Di:
    __instance: 'Di' = None

    @staticmethod
    def instance() -> 'Di':
        if Di.__instance is None:
            Di.__instance = Di()
        return Di.__instance

    # region Managers
    @lazy
    def get_settings_manager(self) -> SettingsManager:
        return SettingsManager(self.get_settings_repository())

    @lazy
    def get_start_manager(self) -> StartManager:
        return StartManager(
            self.get_recipe_repository(),
            self.get_nomenclature_repository(),
            self.get_measurement_unit_storage(),
            self.get_measurement_units_factory(),
            self.get_store_repository()
        )

    @lazy
    def get_nomenclature_manager(self) -> NomenclatureManager:
        return NomenclatureManager(
            nomenclature_repository=self.get_nomenclature_repository(),
            store_repository=self.get_store_repository(),
            recipe_repository=self.get_recipe_repository(),
            nomenclature_storage_finder=self.get_nomenclature_storage_finder(),
        )

    # endregion
    # region Repositories
    @lazy
    def get_settings_repository(self) -> SettingsRepository:
        return SettingsRepository()

    @lazy
    def get_recipe_repository(self) -> RecipeRepository:
        return RecipeRepository(self.get_recipe_storage(), self.get_start_recipes_storage().get_recipes())

    @lazy
    def get_nomenclature_repository(self) -> NomenclatureRepository:
        return NomenclatureRepository(
            self.get_nomenclature_storage(),
            self.get_nomenclature_group_storage(),
            self.get_start_nomenclature_factory().get_nomenclatures(),
            self.get_start_nomenclature_factory().get_nomenclature_groups()
        )

    @lazy
    def get_store_repository(self) -> StoreRepository:
        return StoreRepository(
            self.get_store_transaction_storage(),
            self.get_store_storage(),
            self.get_turnover_storage(),
            self.get_start_store_factory()
        )

    # endregion
    # region Storages

    @lazy
    def get_turnover_storage(self) -> TurnoverStorage:
        return TurnoverStorage()

    @lazy
    def get_recipe_storage(self) -> RecipeStorage:
        return RecipeStorage()

    @lazy
    def get_nomenclature_storage(self) -> NomenclatureStorage:
        return NomenclatureStorage()

    @lazy
    def get_measurement_unit_storage(self) -> MeasurementUnitStorage:
        return MeasurementUnitStorage()

    @lazy
    def get_nomenclature_group_storage(self) -> NomenclatureGroupStorage:
        return NomenclatureGroupStorage()

    @lazy
    def get_store_storage(self) -> StoreStorage:
        return StoreStorage()

    @lazy
    def get_store_transaction_storage(self) -> StoreTransactionStorage:
        return StoreTransactionStorage()

    # endregion
    # region Factories
    @lazy
    def get_report_factory(self) -> ReportFactory:
        return ReportFactory()

    @lazy
    def get_start_nomenclature_factory(self) -> StartNomenclatureFactory:
        return StartNomenclatureFactory(self.get_measurement_units_factory())

    @lazy
    def get_measurement_units_factory(self) -> MeasurementUnitsFactory:
        return MeasurementUnitsFactory()

    @lazy
    def get_start_store_factory(self) -> StartStoreFactory:
        return StartStoreFactory(self.get_start_nomenclature_factory())

    @lazy
    def get_start_recipes_storage(self) -> StartRecipesStorage:
        return StartRecipesStorage(self.get_start_nomenclature_factory(), self.get_measurement_units_factory())

    @lazy
    def get_json_serializer(self) -> JsonSerializer:
        return JsonSerializer()

    @lazy
    def get_nomenclature_storage_finder(self) -> NomenclatureStorageFinder:
        return NomenclatureStorageFinder()

    # endregion
