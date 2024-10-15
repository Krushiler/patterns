from working_with_settings.data.storage.base.base_memory_storage import BaseMemoryStorage
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


class MeasurementUnitStorage(BaseMemoryStorage[str, MeasurementUnit]):
    pass
