from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


class MeasurementUnitsFactory:
    @lazy
    def grams(self) -> MeasurementUnit:
        return MeasurementUnit('гр', 1)

    @lazy
    def things(self) -> MeasurementUnit:
        return MeasurementUnit('шт', 1)

    @lazy
    def tens(self) -> MeasurementUnit:
        return MeasurementUnit('десяток', 10)

    @lazy
    def milliliters(self) -> MeasurementUnit:
        return MeasurementUnit('мл', 1)
