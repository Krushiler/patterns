from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException
from working_with_settings.domain.model.base.base_model import BaseModel


class Store(BaseModel):
    _address: str = None

    def __init__(self, address: str = None):
        super().__init__()

        self.address = address

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._address = value
