from working_with_settings.data.storage.base.base_memory_storage import BaseMemoryStorage
from working_with_settings.domain.model.store.store_turnover import StoreTurnover


class TurnoverStorage(BaseMemoryStorage[float, StoreTurnover]):
    pass
