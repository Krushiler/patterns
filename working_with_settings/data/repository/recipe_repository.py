from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.recipe.recipe import Recipe


class RecipeRepository:

    def __init__(self, recipe_storage: RecipeStorage, start_recipes: list[Recipe]):
        self._recipe_storage = recipe_storage
        self._start_recipes = start_recipes

    def get_recipe(self, recipe_id: str) -> Recipe | None:
        if not isinstance(recipe_id, str):
            raise InvalidTypeException(str, type(recipe_id))
        return self._recipe_storage.get(recipe_id)

    def get_recipes(self) -> list[Recipe]:
        return self._recipe_storage.get_all()

    def generate_start_recipes(self):
        for recipe in self._start_recipes:
            if self._recipe_storage.contains_key(recipe.id):
                continue
            self._recipe_storage.set(recipe.id, recipe)
