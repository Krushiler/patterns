import uuid


class BaseModel:
    def __init__(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        if not isinstance(value, str):
            raise TypeError('id must be str')
        self._id = value

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        if not isinstance(other, BaseModel):
            return False
        return self.id == other.id
