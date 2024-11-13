from working_with_settings.application.base.base_manager import BaseManager
from working_with_settings.application.base.base_state import BaseState
from working_with_settings.data.repository.nomenclature_repository import NomenclatureRepository
from working_with_settings.data.storage_finder.nomenclature.nomenclature_storage_finder import NomenclatureStorageFinder
from working_with_settings.domain.model.organization.nomenclature import Nomenclature
from working_with_settings.util.stream.base.base_observable import StreamSubscription


class NomenclatureManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder

    _nomenclature_updates_subscription: StreamSubscription

    def __init__(self, nomenclature_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder

    def update_nomenclature(self, nomenclature_id: str, nomenclature: Nomenclature):
        self._nomenclature_repository.update_nomenclature(nomenclature_id, nomenclature)

    def delete_nomenclature(self, nomenclature_id: str) -> bool:
        if self._nomenclature_storage_finder.has_nomenclature_dependants(nomenclature_id):
            return False
        self._nomenclature_repository.delete_nomenclature(nomenclature_id)
        return True

    def get_nomenclature(self, nomenclature_id: str):
        return self._nomenclature_repository.get_nomenclature(nomenclature_id)

    def create_nomenclature(self, nomenclature: Nomenclature):
        return self._nomenclature_repository.create_nomenclature(nomenclature)

    def close(self):
        self._nomenclature_updates_subscription.close()
