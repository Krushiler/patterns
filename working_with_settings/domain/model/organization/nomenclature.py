from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException
from working_with_settings.domain.model.base.base_model import BaseModel


class Nomenclature(BaseModel):
    def __init__(self, name: str = '', nomenclature_group_id: str = ''):
        super().__init__()
        self._name = ''
        self._nomenclature_group_id = ''
        self.name = name
        self.nomenclature_group_id = nomenclature_group_id

    @property
    def nomenclature_group_id(self) -> str:
        return self._nomenclature_group_id

    @nomenclature_group_id.setter
    def nomenclature_group_id(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._nomenclature_group_id = value

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
