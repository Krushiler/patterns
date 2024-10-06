from working_with_settings.di.di_utils import lazy
from working_with_settings.domain.model.measurement.measurement_unit import MeasurementUnit


class MeasurementUnitsFactory:

    def get_units(self) -> list[MeasurementUnit]:
        return [
            self.grams(),
            self.kilograms(),
            self.things(),
            self.tens(),
            self.milliliters(),
            self.liter()
        ]

    @lazy
    def grams(self) -> MeasurementUnit:
        return MeasurementUnit('гр', 1)

    @lazy
    def kilograms(self) -> MeasurementUnit:
        return MeasurementUnit('кг', 1000, self.grams())

    @lazy
    def things(self) -> MeasurementUnit:
        return MeasurementUnit('шт', 1)

    @lazy
    def tens(self) -> MeasurementUnit:
        return MeasurementUnit('десяток', 10, self.things())

    @lazy
    def milliliters(self) -> MeasurementUnit:
        return MeasurementUnit('мл', 1)

    @lazy
    def liter(self) -> MeasurementUnit:
        return MeasurementUnit('л', 1000, self.milliliters())
