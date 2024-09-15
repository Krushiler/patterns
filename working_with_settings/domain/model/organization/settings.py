from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException, \
    InvalidFormatException
from working_with_settings.domain.model.base.base_model import BaseModel


class Settings(BaseModel):
    def __init__(self, inn: str = '', bic: str = '', account: str = '', ownership_form: str = ''):
        super().__init__()
        self._inn = ''
        self._bic = ''
        self._account = ''
        self._ownership_form = ''

        self.inn = inn
        self.bic = bic
        self.account = account
        self.ownership_form = ownership_form

    @property
    def inn(self) -> str:
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException('str', type(value))
        if not value.isdigit():
            raise InvalidFormatException('digits', value)
        if len(value) != 12:
            raise InvalidLengthException(12, len(value))
        self._inn = value

    @property
    def bic(self) -> str:
        return self._bic

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._bic = value

    @property
    def account(self) -> str:
        return self._account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._account = value

    @property
    def ownership_form(self) -> str:
        return self._ownership_form

    @ownership_form.setter
    def ownership_form(self, value: str):
        if not isinstance(value, str):
            raise InvalidTypeException(str, type(value))
        self._ownership_form = value
