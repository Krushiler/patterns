import json
import os

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.data.serialization.json_serializer import JsonSerializer
from working_with_settings.util.stream.streams import ValueStream, EventStream


class Dao:
    _full_name: str
    _data: ValueStream[dict[str, dict]]
    _data_updates: EventStream[dict[str, dict]]

    _json_serializer: JsonSerializer

    def __init__(self, file_name, json_serializer):
        self._full_name = os.path.abspath(file_name)
        self._data = ValueStream.seeded({})
        self._data_updates = EventStream()
        self._json_serializer = json_serializer
        self._data_subscription = None

        self._data_updates.subscribe(lambda _: self.flush())

        self.load()

    def flush(self):
        if not os.path.exists(self._full_name):
            os.makedirs(os.path.dirname(self._full_name), exist_ok=True)
        with open(self._full_name, 'w', encoding='utf-8') as f:
            data = json.dumps(self._data.value, ensure_ascii=False, indent=4)
            f.write(data)

    def load(self):
        if os.path.exists(self._full_name):
            with open(self._full_name, 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
                self._data.emit(data)

    def watch_data(self):
        return self._data.as_read_only()

    def save_value(self, key, value):
        data = self._data.value
        data[key] = AbsoluteMapper.to_dict(value)
        self._data.emit(data)
        self._data_updates.emit(data)

    def get_values(self, key: str, dtype: type) -> dict:
        if key not in self._data.value:
            return {}

        result = {}

        item_dict = self._data.value[key]

        for key, value in item_dict.items():
            item = self._json_serializer.deserialize(value, dtype)
            result[key] = item

        return result
