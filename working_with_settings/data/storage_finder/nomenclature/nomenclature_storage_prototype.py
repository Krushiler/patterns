from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.data.storage.store_transaction_storage import StoreTransactionStorage
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.domain.model.filter.filter_type import FilterType
from working_with_settings.domain.model.recipe.recipe import Recipe

T = TypeVar('T')


class NomenclatureStoragePrototype(Generic[T], ABC):

    @abstractmethod
    def find(self, nomenclature_id) -> T:
        pass

    @staticmethod
    def _create_nomenclature_filter(key: str, nomenclature_id: str) -> Filter:
        return Filter(
            key,
            nomenclature_id,
            filter_type=FilterType.EQUALS
        )


class RecipePrototype(NomenclatureStoragePrototype[list[Recipe]]):
    _recipe_storage: RecipeStorage

    def __init__(self, recipe_storage):
        self._recipe_storage = recipe_storage

    def find(self, nomenclature_id) -> list[Recipe]:
        return self._recipe_storage.get_filtered([
            self._create_nomenclature_filter('ingredients.nomenclature.id', nomenclature_id)
        ])


class StoreTransactionPrototype(NomenclatureStoragePrototype[list[Recipe]]):
    _transaction_storage: StoreTransactionStorage

    def __init__(self, transaction_storage):
        self._transaction_storage = transaction_storage

    def find(self, nomenclature_id) -> list[Recipe]:
        return self._transaction_storage.get_filtered([
            self._create_nomenclature_filter('nomenclature.id', nomenclature_id)
        ])
