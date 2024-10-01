from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel


class NomenclatureGroup(BaseModel):
    _name: str = None

    def __init__(self, name: str = None):
        super().__init__()
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._name = value
