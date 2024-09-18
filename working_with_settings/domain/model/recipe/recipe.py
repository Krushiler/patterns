from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel
import datetime

from working_with_settings.domain.model.recipe.ingredient import Ingredient


class Recipe(BaseModel):
    def __init__(self, name: str = '', cooking_time: datetime.timedelta = None, ingredients: list[Ingredient] = None,
                 cooking_steps: list[str] = None):
        super().__init__()

        self._name = ''
        self._cooking_time = None
        self._ingredients = None
        self._cooking_steps = None

        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.cooking_steps = cooking_steps

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._name = value

    @property
    def cooking_time(self) -> datetime.timedelta | None:
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value: datetime.timedelta):
        if value is None:
            return
        if not isinstance(value, datetime.timedelta):
            raise InvalidTypeException(datetime.timedelta, type(value))
        self._cooking_time = value

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value: list[Ingredient]):
        if not isinstance(value, list):
            raise InvalidTypeException(list, type(value))
        if not all(isinstance(x, Ingredient) for x in value):
            raise InvalidTypeException(Ingredient, type(value))
        self._ingredients = value

    @property
    def cooking_steps(self) -> list[str]:
        return self._cooking_steps

    @cooking_steps.setter
    def cooking_steps(self, value: list[str]):
        if not isinstance(value, list):
            raise InvalidTypeException(list, type(value))
        if not all(isinstance(x, str) for x in value):
            raise InvalidTypeException(str, type(value))
        self._cooking_steps = value
