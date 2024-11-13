from enum import Enum

from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.data.storage_finder.nomenclature.nomenclature_storage_prototype import \
    NomenclatureStoragePrototype, StoreTransactionPrototype, RecipePrototype
from working_with_settings.domain.model.recipe.recipe import Recipe
from working_with_settings.domain.model.store.store_transaction import StoreTransaction


class NomenclatureDependantType(Enum):
    STORE_TRANSACTION = 0
    RECIPE = 1


class NomenclatureStorageFinder:
    _finders: dict[NomenclatureDependantType, NomenclatureStoragePrototype]

    def __init__(self, transaction_storage: StoreTransactionStorage, recipe_storage: RecipeStorage):
        self._finders = {
            NomenclatureDependantType.STORE_TRANSACTION: StoreTransactionPrototype(transaction_storage),
            NomenclatureDependantType.RECIPE: RecipePrototype(recipe_storage)
        }

    def find_dependant_recipes(self, nomenclature_id: str) -> list[Recipe]:
        return self._finders[NomenclatureDependantType.RECIPE].find(nomenclature_id)

    def find_dependant_transactions(self, nomenclature_id: str) -> list[StoreTransaction]:
        return self._finders[NomenclatureDependantType.STORE_TRANSACTION].find(nomenclature_id)

    def has_nomenclature_dependants(self, nomenclature_id: str) -> bool:
        return any([len(finder.find(nomenclature_id)) > 0 for finder in self._finders.values()])
