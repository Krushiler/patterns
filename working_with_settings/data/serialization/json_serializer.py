import io
import json

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper
from working_with_settings.data.serialization.base.base_serializer import BaseSerializer


class JsonSerializer(BaseSerializer[str]):
    def deserialize(self, data: str, cls: type):
        json_data = json.loads(data.encode('utf-8'))

        if isinstance(json_data, list):
            return [AbsoluteMapper.from_dict(item, cls) for item in json_data]
        return AbsoluteMapper.from_dict(json_data, cls)

    def serialize(self, obj) -> str:
        if isinstance(obj, list):
            data = [AbsoluteMapper.to_dict(item) for item in obj]
        else:
            data = AbsoluteMapper.to_dict(obj)
        return json.dumps(data, default=str, ensure_ascii=False)
