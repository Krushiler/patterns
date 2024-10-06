from working_with_settings.data.factory.measurement_units_factory import MeasurementUnitsFactory
from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.domain.model.organization.nomenclature_group import NomenclatureGroup


class StartNomenclatureFactory:

    def __init__(self, unitsFactory: MeasurementUnitsFactory):
        self._unitsFactory = unitsFactory

    @lazy
    def nomenclature_group(self) -> NomenclatureGroup:
        return NomenclatureGroup('Еда')

    @lazy
    def wheat_flour(self) -> Nomenclature:
        return Nomenclature('Пшеничная мука', self._unitsFactory.kilograms(), self.nomenclature_group())

    @lazy
    def milk(self) -> Nomenclature:
        return Nomenclature('Молоко', self._unitsFactory.liter(), self.nomenclature_group())

    @lazy
    def egg(self) -> Nomenclature:
        return Nomenclature('Яйцо', self._unitsFactory.tens(), self.nomenclature_group())

    @lazy
    def sugar(self) -> Nomenclature:
        return Nomenclature('Сахар', self._unitsFactory.kilograms(), self.nomenclature_group())

    @lazy
    def baking_powder(self) -> Nomenclature:
        return Nomenclature('Разрыхлитель', self._unitsFactory.kilograms(), self.nomenclature_group())

    @lazy
    def butter(self) -> Nomenclature:
        return Nomenclature('Сливочное масло', self._unitsFactory.kilograms(), self.nomenclature_group())

    @lazy
    def salt(self) -> Nomenclature:
        return Nomenclature('Соль', self._unitsFactory.kilograms(), self.nomenclature_group())

    @lazy
    def vanilla_sugar(self) -> Nomenclature:
        return Nomenclature('Ванильный сахар', self._unitsFactory.kilograms(), self.nomenclature_group())
