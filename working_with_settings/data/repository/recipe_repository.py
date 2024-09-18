from working_with_settings.data.factory.base.base_recipe_factory import BaseRecipeFactory
from working_with_settings.data.storage.recipe_storage import RecipeStorage
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.recipe.recipe import Recipe


class RecipeRepository:

    def __init__(self, recipe_storage: RecipeStorage, recipe_factories: list[BaseRecipeFactory]):
        self._recipe_storage = recipe_storage
        self._recipe_factories = recipe_factories

        self._generate_recipes()

    def get_recipe(self, recipe_id: str) -> Recipe | None:
        if not isinstance(recipe_id, str):
            raise InvalidTypeException(str, type(recipe_id))
        return self._recipe_storage.get(recipe_id)

    def get_recipes(self) -> list[Recipe]:
        return self._recipe_storage.get_all()

    def _generate_recipes(self):
        for recipe_factory in self._recipe_factories:
            recipe = recipe_factory.recipe()
            self._recipe_storage.set(recipe.id, recipe)
