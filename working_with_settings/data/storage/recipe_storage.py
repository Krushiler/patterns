from working_with_settings.data.storage.base.base_memory_storage import BaseMemoryStorage
from working_with_settings.domain.model.recipe.recipe import Recipe


class RecipeStorage(BaseMemoryStorage[str, Recipe]):
    pass
