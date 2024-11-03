from working_with_settings.data.storage.base.base_storage import BaseStorage
from working_with_settings.di.di import Di
from working_with_settings.domain.exceptions.base.either import Either
from working_with_settings.routing.util.response_factory import ResponseFactory


class StorageFactory:
    _storages_map = {
        'recipe': Di.instance().get_recipe_storage(),
        'nomenclature': Di.instance().get_nomenclature_storage(),
        'nomenclature-group': Di.instance().get_nomenclature_group_storage(),
        'unit': Di.instance().get_measurement_unit_storage(),
        'store': Di.instance().get_store_storage(),
        'store-transaction': Di.instance().get_store_transaction_storage(),
    }

    @classmethod
    def get_storage(cls, model_name: str) -> Either[object, BaseStorage]:
        if model_name not in cls._storages_map:
            return Either.with_left(ResponseFactory.error('Unknown entity: {}'.format(model_name)))
        return Either.with_right(cls._storages_map.get(model_name))
