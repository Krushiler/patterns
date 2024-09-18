from abc import ABC, abstractmethod

from working_with_settings.domain.model.recipe.recipe import Recipe


class BaseRecipeFactory(ABC):
    @abstractmethod
    def recipe(self) -> Recipe:
        pass
