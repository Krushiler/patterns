from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.repository.recipe_repository import RecipeRepository


class StartManager(BaseManager[BaseState]):
    def __init__(self, recipe_repository: RecipeRepository):
        super().__init__(BaseState())

        self._recipe_repository = recipe_repository

    def init(self):
        self._recipe_repository.init_start_recipes()
