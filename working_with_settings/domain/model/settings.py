from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException, \
    InvalidFormatException
from working_with_settings.domain.model.base.base_model import BaseModel


class Settings(BaseModel):
    def __init__(self):
        super().__init__()
        self._organization_name = ''
        self._inn = ''
        self._director_name = ''

    @property
    def organization_name(self):
        return self._organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._organization_name = value

    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        if not value.isdigit():
            raise InvalidFormatException('digits', value)
        if len(value) != 12:
            raise InvalidLengthException(12, len(value))
        self._inn = value

    @property
    def director_name(self):
        return self._director_name

    @director_name.setter
    def director_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('director_name must be str')
        self._director_name = value
