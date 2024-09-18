import datetime

from working_with_settings.data.factory.base.base_recipe_factory import BaseRecipeFactory
from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.recipe.ingredient import Ingredient
from working_with_settings.domain.model.recipe.recipe import Recipe


class MilkPancakesRecipeFactory(BaseRecipeFactory):
    def __init__(self, nomenclature_factory: StartNomenclatureFactory, unit_factory: MeasurementUnitsFactory):
        self._nomenclature_factory = nomenclature_factory
        self._unit_factory = unit_factory

    @lazy
    def ingredients(self) -> list[Ingredient]:
        return [
            Ingredient(self._nomenclature_factory.wheat_flour(), MeasuredValue(150, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.milk(), MeasuredValue(200, self._unit_factory.milliliters())),
            Ingredient(self._nomenclature_factory.egg(), MeasuredValue(1, self._unit_factory.things())),
            Ingredient(self._nomenclature_factory.sugar(), MeasuredValue(50, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.baking_powder(), MeasuredValue(10, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.butter(), MeasuredValue(50, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.salt(), MeasuredValue(2, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.vanilla_sugar(), MeasuredValue(10, self._unit_factory.grams())),
        ]

    @lazy
    def recipe(self) -> Recipe:
        return Recipe(name='Панкейки на молоке', ingredients=self.ingredients(),
                      cooking_time=datetime.timedelta(minutes=25), cooking_steps=[
                'Как приготовить панкейки на молоке? Подготовьте все необходимые ингредиенты. Порции рассчитаны '
                'примерно на 10 небольших панкейков диаметром около 8 см.',

                'В глубокой миске взбейте яйцо с сахаром и ванильным сахаром до легкой пены.',

                'Добавьте в смесь молоко и размешайте венчиком до однородности.',

                'Растопите сливочное масло на слабом огне или в микроволновке, дайте ему немного остыть и добавьте в '
                'смесь. Снова перемешайте.',

                'В отдельной миске просейте муку вместе с разрыхлителем и солью.',

                'Постепенно добавляйте сухие ингредиенты в жидкую смесь, постоянно помешивая венчиком, чтобы избежать '
                'комочков. В итоге у вас должно получиться однородное, густое тесто.',

                'Разогрейте сковороду на среднем огне, слегка смажьте ее маслом. Для жарки панкейков можно '
                'использовать совсем немного масла, чтобы они не были слишком жирными.',

                'Вылейте небольшое количество теста на сковороду, формируя круглые лепешки. Жарьте на среднем огне до '
                'появления пузырьков на поверхности, затем аккуратно переверните и поджарьте с другой стороны до '
                'золотистого цвета.',

                'Подавайте панкейки с медом, ягодами, сиропом или сметаной по вкусу.'
            ])
