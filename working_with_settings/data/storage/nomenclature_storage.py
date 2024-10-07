from working_with_settings.data.storage.base.base_memory_storage import BaseMemoryStorage
from working_with_settings.domain.model.organization.nomenclature import Nomenclature


class NomenclatureStorage(BaseMemoryStorage[str, Nomenclature]):
    pass
