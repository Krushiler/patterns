from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.recipe_repository import RecipeRepository
from working_with_settings.data.storage_finder.nomenclature.nomenclature_storage_finder import NomenclatureStorageFinder
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.util.stream.base.base_observable import StreamSubscription


class RecipeManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _recipe_repository: RecipeRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder

    _nomenclature_updates_subscription: StreamSubscription

    def __init__(self, nomenclature_repository, recipe_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._recipe_repository = recipe_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder

    def init(self):
        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates() \
            .subscribe(self._on_nomenclature_updated)

    def _on_nomenclature_updated(self, nomenclature: Nomenclature):
        recipes = self._nomenclature_storage_finder.find_dependant_recipes(nomenclature.id)

        for recipe in recipes:
            for ingredient in recipe.ingredients:
                if ingredient.nomenclature.id == nomenclature.id:
                    ingredient.nomenclature = nomenclature
            self._recipe_repository.update_recipe(recipe.id, recipe)

    def close(self):
        self._nomenclature_updates_subscription.close()
