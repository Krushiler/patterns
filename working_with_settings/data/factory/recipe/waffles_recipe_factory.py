import datetime

from working_with_settings.data.factory.base.base_recipe_factory import BaseRecipeFactory
from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.recipe.ingredient import Ingredient
from working_with_settings.domain.model.recipe.recipe import Recipe


class WafflesRecipeFactory(BaseRecipeFactory):

    def __init__(self, nomenclature_factory: StartNomenclatureFactory, unit_factory: MeasurementUnitsFactory):
        self._nomenclature_factory = nomenclature_factory
        self._unit_factory = unit_factory

    def recipe(self) -> Recipe:
        return Recipe(name='ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ', ingredients=[
            Ingredient(self._nomenclature_factory.wheat_flour(), MeasuredValue(100, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.sugar(), MeasuredValue(80, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.butter(), MeasuredValue(70, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.egg(), MeasuredValue(1, self._unit_factory.things())),
            Ingredient(self._nomenclature_factory.vanilla_sugar(), MeasuredValue(5, self._unit_factory.grams())),
        ], cooking_time=datetime.timedelta(minutes=20), cooking_steps=[
            'Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня '
            'получилось 8 штук диаметром около 10 см.',

            'Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо '
            'в микроволновке.',

            'Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар '
            'довольно быстро растает.',

            'Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может '
            'свариться. Перемешайте яйцо с маслом до однородности.',

            'Всыпьте муку, добавьте ванилин.',

            'Перемешайте массу венчиком до состояния гладкого однородного теста.',

            'Разогрейте вафельницу по инструкции к ней. У меня очень старая, еще советских времен электровафельница. '
            'Она может и не очень красивая, но печет замечательно! Я не смазываю вафельницу маслом, '
            'в тесте достаточно жира, да и к ней уже давно ничего не прилипает. Но вы смотрите по своей модели. '
            'Выкладывайте тесто по столовой ложке. Можно класть немного меньше теста, тогда вафли будут меньше и их '
            'получится больше.',

            'Пеките вафли несколько минут до золотистого цвета. Осторожно откройте вафельницу, она очень горячая! '
            'Снимите вафлю лопаткой. Горячая она очень мягкая, как блинчик.'
        ])
