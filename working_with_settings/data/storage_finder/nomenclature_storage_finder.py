from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.di.di import Di
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.recipe.recipe import Recipe
from working_with_settings.domain.model.store.store_transaction import StoreTransaction


class NomenclatureDependants:
    _recipes: list[Recipe]
    _transactions: list[StoreTransaction]

    def __init__(self, recipes: list[Recipe], transactions: list[StoreTransaction]):
        self._recipes = recipes
        self._transactions = transactions

    @property
    def recipes(self) -> list[Recipe]:
        return self._recipes

    @property
    def transactions(self) -> list[StoreTransaction]:
        return self._transactions

    @property
    def is_empty(self):
        return len(self.recipes) == 0 and len(self.transactions) == 0


class NomenclatureStorageFinder:
    _transaction_storage: StoreTransactionStorage
    _recipe_storage: RecipeStorage

    def __init__(self):
        self._transaction_storage = Di.instance().get_store_transaction_storage()
        self._recipe_storage = Di.instance().get_recipe_storage()

    @staticmethod
    def _create_nomenclature_filter(key: str, nomenclature_id: str) -> Filter:
        return Filter(
            key,
            nomenclature_id,
            filter_type=FilterType.EQUALS
        )

    def find_nomenclature_dependencies(self, nomenclature_id: str) -> NomenclatureDependants:
        recipes = self._recipe_storage.get_filtered(
            self._create_nomenclature_filter('ingredients.nomenclature.id', nomenclature_id)
        )
        transactions = self._transaction_storage.get_filtered(
            self._create_nomenclature_filter('nomenclature.id', nomenclature_id)
        )
        return NomenclatureDependants(recipes=recipes, transactions=transactions)
