from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException
from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit
from working_with_settings.domain.model.organization.nomenclature_group import NomenclatureGroup


class Nomenclature(BaseModel):
    _name: str = None
    _unit: MeasurementUnit = None
    _nomenclature_group: NomenclatureGroup = None

    def __init__(self, name: str = None, unit: MeasurementUnit = None, nomenclature_group: NomenclatureGroup = None):
        super().__init__()

        self.name = name
        self.unit = unit
        self.nomenclature_group = nomenclature_group

    @property
    def nomenclature_group(self) -> str:
        return self._nomenclature_group

    @nomenclature_group.setter
    def nomenclature_group(self, value: str):
        if value is None:
            return
        if not isinstance(value, NomenclatureGroup):
            raise InvalidTypeException(str, type(value))
        self._nomenclature_group = value

    @property
    def unit(self) -> MeasurementUnit:
        return self._unit

    @unit.setter
    def unit(self, value: MeasurementUnit):
        if value is None:
            return
        if not isinstance(value, MeasurementUnit):
            raise InvalidTypeException(MeasurementUnit, type(value))
        self._unit = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        if len(value) > 255:
            raise InvalidLengthException(255, len(value))
        self._name = value
