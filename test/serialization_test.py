from working_with_settings.di.di import Di
from working_with_settings.domain.model.measurement.measured_value import MeasuredValue


def process_serialization(obj, inject: Di):
    json_serializer = inject.get_json_serializer()

    serialized = json_serializer.serialize(obj)

    if isinstance(obj, list):
        t = type(obj[0])
    else:
        t = type(obj)

    deserialized = json_serializer.deserialize(serialized, t)

    return deserialized


def test_nomenclature_serialization(inject: Di):
    nomenclature = inject.get_start_nomenclature_factory().sugar()
    deserialized = process_serialization(nomenclature, inject)

    assert nomenclature == deserialized


def test_measurement_value_serialization(inject: Di):
    value = MeasuredValue(10, inject.get_measurement_units_factory().kilograms())
    deserialized = process_serialization(value, inject)

    assert value == deserialized


def test_list_measured_value_serialization(inject: Di):
    values = [
        MeasuredValue(10, inject.get_measurement_units_factory().kilograms()),
        MeasuredValue(100, inject.get_measurement_units_factory().liter())
    ]

    deserialized = process_serialization(values, inject)

    assert deserialized[0].unit == values[0].unit
    assert deserialized[0].value == values[0].value

    assert deserialized[1].unit == values[1].unit
    assert deserialized[1].value == values[1].value
