from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.repository.recipe_repository import RecipeRepository


class StartManager(BaseManager[BaseState]):
    def __init__(self, recipe_repository: RecipeRepository, nomenclature_repository: NomenclatureRepository):
        super().__init__(BaseState())

        self._recipe_repository = recipe_repository
        self._nomenclature_repository = nomenclature_repository

    def init(self):
        self._recipe_repository.init_start_recipes()
        self._nomenclature_repository.init_start_nomenclature()
