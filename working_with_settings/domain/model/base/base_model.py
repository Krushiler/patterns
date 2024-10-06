import uuid

from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException


class BaseModel:
    _id: str = None

    def __init__(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        if value is None:
            return
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._id = value

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        if not isinstance(other, BaseModel):
            return False
        return self.id == other.id
