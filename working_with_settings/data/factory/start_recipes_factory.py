import datetime

from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.data.factory.start_nomenclature_factory import StartNomenclatureFactory
from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue
from working_with_settings.domain.model.recipe.ingredient import Ingredient
from working_with_settings.domain.model.recipe.recipe import Recipe


class StartRecipesFactory:
    def __init__(self, nomenclature_factory: StartNomenclatureFactory, unit_factory: MeasurementUnitsFactory):
        self._nomenclature_factory = nomenclature_factory
        self._unit_factory = unit_factory

    def get_recipes(self) -> list[Recipe]:
        return [
            self._build_pancakes_recipe(),
            self._build_waffles_recipe()
        ]

    @lazy
    def _build_pancakes_recipe(self) -> Recipe:
        return Recipe(name='Панкейки на молоке', ingredients=[
            Ingredient(self._nomenclature_factory.wheat_flour(), MeasuredValue(150, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.milk(), MeasuredValue(200, self._unit_factory.milliliters())),
            Ingredient(self._nomenclature_factory.egg(), MeasuredValue(1, self._unit_factory.things())),
            Ingredient(self._nomenclature_factory.sugar(), MeasuredValue(50, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.baking_powder(), MeasuredValue(10, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.butter(), MeasuredValue(50, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.salt(), MeasuredValue(2, self._unit_factory.grams())),
            Ingredient(self._nomenclature_factory.vanilla_sugar(), MeasuredValue(10, self._unit_factory.grams())),
        ],
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

    @lazy
    def _build_waffles_recipe(self) -> Recipe:
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
