from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class StartNomenclatureFactory:

    def __init__(self, unitsFactory: MeasurementUnitsFactory):
        self._unitsFactory = unitsFactory

    @lazy
    def wheat_flour(self) -> Nomenclature:
        return Nomenclature('Пшеничная мука', self._unitsFactory.kilograms())

    @lazy
    def milk(self) -> Nomenclature:
        return Nomenclature('Молоко', self._unitsFactory.liter())

    @lazy
    def egg(self) -> Nomenclature:
        return Nomenclature('Яйцо', self._unitsFactory.tens())

    @lazy
    def sugar(self) -> Nomenclature:
        return Nomenclature('Сахар', self._unitsFactory.kilograms())

    @lazy
    def baking_powder(self) -> Nomenclature:
        return Nomenclature('Разрыхлитель', self._unitsFactory.kilograms())

    @lazy
    def butter(self) -> Nomenclature:
        return Nomenclature('Сливочное масло', self._unitsFactory.kilograms())

    @lazy
    def salt(self) -> Nomenclature:
        return Nomenclature('Соль', self._unitsFactory.kilograms())

    @lazy
    def vanilla_sugar(self) -> Nomenclature:
        return Nomenclature('Ванильный сахар', self._unitsFactory.kilograms())
