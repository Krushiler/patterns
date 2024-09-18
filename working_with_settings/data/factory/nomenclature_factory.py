from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class NomenclatureFactory:

    @lazy
    def wheat_flour(self) -> Nomenclature:
        return Nomenclature('Пшеничная мука')

    @lazy
    def milk(self) -> Nomenclature:
        return Nomenclature('Молоко')

    @lazy
    def egg(self) -> Nomenclature:
        return Nomenclature('Яйцо')

    @lazy
    def sugar(self) -> Nomenclature:
        return Nomenclature('Сахар')

    @lazy
    def baking_powder(self) -> Nomenclature:
        return Nomenclature('Разрыхлитель')

    @lazy
    def butter(self) -> Nomenclature:
        return Nomenclature('Сливочное масло')

    @lazy
    def salt(self) -> Nomenclature:
        return Nomenclature('Соль')

    @lazy
    def vanilla_sugar(self) -> Nomenclature:
        return Nomenclature('Ванильный сахар')
