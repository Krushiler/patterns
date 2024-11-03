from working_with_settings.data.storage.base.base_memory_storage import BaseMemoryStorage
from working_with_settings.domain.model.store.store_transaction import StoreTransaction


class StoreTransactionStorage(BaseMemoryStorage[str, StoreTransaction]):
    pass
