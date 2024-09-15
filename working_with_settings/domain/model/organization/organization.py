from working_with_settings.domain.model.base.base_model import BaseModel
from working_with_settings.domain.model.organization.settings import Settings


class Organization(BaseModel):
    def __init__(self, settings: Settings):
        super().__init__()
        self._inn = settings.inn
        self._bic = settings.bic
        self._account = settings.account
        self._ownership_form = settings.ownership_form

    @property
    def inn(self) -> str:
        return self._inn

    @property
    def bic(self) -> str:
        return self._bic

    @property
    def account(self) -> str:
        return self._account

    @property
    def ownership_form(self) -> str:
        return self._ownership_form
