from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.recipe_repository import RecipeRepository
from working_with_settings.data.repository.store_repository import StoreRepository
from working_with_settings.data.storage_finder.nomenclature_storage_finder import NomenclatureStorageFinder
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.util.stream.stream_subscription import StreamSubscription


class NomenclatureManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _recipe_repository: RecipeRepository
    _store_repository: StoreRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder

    _nomenclature_updates_subscription: StreamSubscription

    def __init__(self, nomenclature_repository, recipe_repository, store_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._recipe_repository = recipe_repository
        self._store_repository = store_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder

        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates().subscribe(
            self._on_nomenclature_updated
        )

    def _on_nomenclature_updated(self, nomenclature: Nomenclature):
        dependants = self._nomenclature_storage_finder.find_nomenclature_dependencies(nomenclature.id)

        for recipe in dependants.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.nomenclature.id == nomenclature.id:
                    ingredient.nomenclature = nomenclature
            self._recipe_repository.update_recipe(recipe.id, recipe)

        for transaction in dependants.transactions:
            transaction.nomenclature = nomenclature

    def update_nomenclature(self, nomenclature_id: str, nomenclature: Nomenclature):
        self._nomenclature_repository.update_nomenclature(nomenclature_id, nomenclature)

    def delete_nomenclature(self, nomenclature_id: str) -> bool:
        dependants = self._nomenclature_storage_finder.find_nomenclature_dependencies(nomenclature_id)
        if dependants.is_empty:
            self._nomenclature_repository.delete_nomenclature(nomenclature_id)
            return True
        return False

    def get_nomenclature(self, nomenclature_id: str):
        return self._nomenclature_repository.get_nomenclature(nomenclature_id)

    def create_nomenclature(self, nomenclature: Nomenclature):
        return self._nomenclature_repository.create_nomenclature(nomenclature)

    def close(self):
        self._nomenclature_updates_subscription.close()
