from abc import ABC

from working_with_settings.data.storage.base.base_storage import BaseStorage, K, V
from working_with_settings.data.storage.database.dao import Dao
from working_with_settings.data.storage.filterer.list_filterer import ListFilterer
from working_with_settings.domain.model.filter.filter import Filter
from working_with_settings.util.logging.logger import Logger


class BaseMemoryStorage(BaseStorage[K, V], ABC):
    _dao: Dao
    _data: dict[K, V]

    def __init__(self, dao: Dao):
        super().__init__()
        self._dao = dao
        self._data = {}
        self._dao.watch_data().subscribe(lambda _: self._load_from_dao())

    @property
    def _key(self):
        return self.__class__.__name__

    def _load_from_dao(self):
        self._data = self._dao.get_values(self._key, self._type_V)

    def _commit_to_dao(self):
        self._dao.save_value(self._key, self._data)

    def contains_key(self, key: K) -> bool:
        return key in self._data

    def get(self, key: K) -> V | None:
        self._dao.load()
        return self._data.get(key)

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        self._dao.load()
        values = list(self._data.values())
        if limit is not None:
            values = values[offset:offset + limit]
        else:
            values = values[offset:]
        return values

    def create(self, value: V):
        self._data[value.id] = value
        self._commit_to_dao()
        Logger.info(self._key, f"Created {value.id}")

    def _update_internal(self, key: K, value: V):
        self._data[key] = value
        self._commit_to_dao()
        Logger.info(self._key, f"Updated {value.id}")

    def _delete_internal(self, key: K):
        if key in self._data:
            del self._data[key]
            Logger.info(self._key, f"Deleted {key}")
        else:
            Logger.info(self._key, f"Could not delete {key} because it does not exist")
        self._commit_to_dao()

    def clear(self):
        self._data.clear()
        self._commit_to_dao()
        Logger.info(self._key, "Cleared")

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def get_filtered(self, filters: list[Filter]) -> list[V]:
        return ListFilterer.apply_filters(self._data.values(), filters)
