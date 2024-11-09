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


class Di:
    __instance: 'Di' = None

    @staticmethod
    def instance() -> 'Di':
        if Di.__instance is None:
            Di.__instance = Di()
        return Di.__instance

    def __init__(self):
        # region Factories
        self._measurement_units_factory = None
        self._start_nomenclature_factory = None
        self._report_factory = None
        self._start_store_factory = None
        # endregion
        # region Managers
        self._settings_manager = None
        self._start_manager = None
        # endregion
        # region Repositories
        self._settings_repository = None
        self._nomenclature_repository = None
        self._recipe_repository = None
        self._store_repository = None
        # endregion
        # region Storages
        self._recipe_storage = None
        self._nomenclature_storage = None
        self._nomenclature_group_storage = None
        self._start_recipes_storage = None
        self._measurement_unit_storage = None
        self._store_storage = None
        self._store_transaction_storage = None
        self._turnover_storage = None
        # endregion

    # region Managers
    def get_settings_manager(self) -> SettingsManager:
        if self._settings_manager is None:
            self._settings_manager = SettingsManager(self.get_settings_repository())

        return self._settings_manager

    def get_start_manager(self) -> StartManager:
        if self._start_manager is None:
            self._start_manager = StartManager(self.get_recipe_repository(), self.get_nomenclature_repository(),
                                               self.get_measurement_unit_storage(),
                                               self.get_measurement_units_factory(),
                                               self.get_store_repository())

        return self._start_manager

    # endregion
    # region Repositories
    def get_settings_repository(self) -> SettingsRepository:
        if self._settings_repository is None:
            self._settings_repository = SettingsRepository()
        return self._settings_repository

    def get_recipe_repository(self) -> RecipeRepository:
        if self._recipe_repository is None:
            self._recipe_repository = RecipeRepository(
                self.get_recipe_storage(),
                self.get_start_recipes_storage().get_recipes())

        return self._recipe_repository

    def get_nomenclature_repository(self) -> NomenclatureRepository:
        if self._nomenclature_repository is None:
            self._nomenclature_repository = NomenclatureRepository(
                self.get_nomenclature_storage(),
                self.get_nomenclature_group_storage(),
                self.get_start_nomenclature_factory().get_nomenclatures(),
                self.get_start_nomenclature_factory().get_nomenclature_groups())

        return self._nomenclature_repository

    def get_store_repository(self) -> StoreRepository:
        if self._store_repository is None:
            self._store_repository = StoreRepository(
                self.get_store_transaction_storage(),
                self.get_store_storage(),
                self.get_turnover_storage(),
                self.get_start_store_factory())

        return self._store_repository

    # endregion
    # region Storages

    def get_turnover_storage(self) -> TurnoverStorage:
        if self._turnover_storage is None:
            self._turnover_storage = TurnoverStorage()

        return self._turnover_storage

    def get_recipe_storage(self) -> RecipeStorage:
        if self._recipe_storage is None:
            self._recipe_storage = RecipeStorage()

        return self._recipe_storage

    def get_nomenclature_storage(self) -> NomenclatureStorage:
        if self._nomenclature_storage is None:
            self._nomenclature_storage = NomenclatureStorage()

        return self._nomenclature_storage

    def get_measurement_unit_storage(self) -> MeasurementUnitStorage:
        if self._measurement_unit_storage is None:
            self._measurement_unit_storage = MeasurementUnitStorage()

        return self._measurement_unit_storage

    def get_nomenclature_group_storage(self) -> NomenclatureGroupStorage:
        if self._nomenclature_group_storage is None:
            self._nomenclature_group_storage = NomenclatureGroupStorage()

        return self._nomenclature_group_storage

    def get_store_storage(self) -> StoreStorage:
        if self._store_storage is None:
            self._store_storage = StoreStorage()

        return self._store_storage

    def get_store_transaction_storage(self) -> StoreTransactionStorage:
        if self._store_transaction_storage is None:
            self._store_transaction_storage = StoreTransactionStorage()

        return self._store_transaction_storage

    # endregion
    # region Factories
    def get_report_factory(self) -> ReportFactory:
        if self._report_factory is None:
            self._report_factory = ReportFactory()

        return self._report_factory

    def get_start_nomenclature_factory(self) -> StartNomenclatureFactory:
        if self._start_nomenclature_factory is None:
            self._start_nomenclature_factory = StartNomenclatureFactory(self.get_measurement_units_factory())

        return self._start_nomenclature_factory

    def get_measurement_units_factory(self) -> MeasurementUnitsFactory:
        if self._measurement_units_factory is None:
            self._measurement_units_factory = MeasurementUnitsFactory()

        return self._measurement_units_factory

    def get_start_store_factory(self) -> StartStoreFactory:
        if self._start_store_factory is None:
            self._start_store_factory = StartStoreFactory(self.get_start_nomenclature_factory())

        return self._start_store_factory

    def get_start_recipes_storage(self) -> StartRecipesStorage:
        if self._start_recipes_storage is None:
            self._start_recipes_storage = StartRecipesStorage(self.get_start_nomenclature_factory(),
                                                              self.get_measurement_units_factory())

        return self._start_recipes_storage

    def get_json_serializer(self) -> JsonSerializer:
        return JsonSerializer()

    # endregion
