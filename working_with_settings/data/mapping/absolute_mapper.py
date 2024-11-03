from enum import Enum

from working_with_settings.data.mapping.type_mapping.timedelta_mapper import TimedeltaMapper
from working_with_settings.domain.model.base.base_model import BaseModel
from typing import get_type_hints, get_args, get_origin


class AbsoluteMapper:
    _primitives = (bool, str, int, float, type(None))

    _mappers = [
        TimedeltaMapper()
    ]

    @staticmethod
    def from_dict(dictionary: dict | object, cls: type):
        if dictionary is None:
            return None

        for mapper in AbsoluteMapper._mappers:
            if issubclass(cls, get_args(type(mapper).__orig_bases__[0])[0]):
                return mapper.to_model(dictionary)

        if cls in AbsoluteMapper._primitives:
            return dictionary

        if get_origin(cls) == list:
            inner_type = get_args(cls)[0]
            return [AbsoluteMapper.from_dict(item, inner_type) for item in dictionary]

        obj = cls.__new__(cls, cls)

        class_fields = get_type_hints(cls)

        for field in dictionary.keys():
            type_hint_name = f'_{field}'

            if type_hint_name not in class_fields.keys():
                continue

            field_class = class_fields[type_hint_name]

            if issubclass(field_class, Enum):
                for value in field_class.__members__.values():
                    if value.value == dictionary[field] or value.name == dictionary[field]:
                        setattr(obj, field, value)
                        break

                continue

            setattr(obj, field, AbsoluteMapper.from_dict(dictionary[field], class_fields[type_hint_name]))

        return obj

    @staticmethod
    def to_dict(obj) -> dict:

        if isinstance(obj, list):
            return [AbsoluteMapper.to_dict(item) for item in obj]

        def get_properties(obj):
            if hasattr(obj, '__dict__'):
                return dict(
                    (x, getattr(obj, x)) for x in obj.__class__.__dict__ if
                    isinstance(obj.__class__.__dict__[x], property))
            else:
                return obj

        if type(obj) in AbsoluteMapper._primitives:
            return obj

        props = get_properties(obj)

        if isinstance(obj, BaseModel):
            props['id'] = obj.id

        for prop in props:
            for mapper in AbsoluteMapper._mappers:
                if isinstance(props[prop], get_args(type(mapper).__orig_bases__[0])[0]):
                    props[prop] = mapper.from_model(props[prop])
                    continue

            if isinstance(props[prop], list):
                new_list = []
                for item in props[prop]:
                    new_list.append(AbsoluteMapper.to_dict(item))
                props[prop] = new_list
            elif hasattr(props[prop], '__dict__'):
                props[prop] = AbsoluteMapper.to_dict(props[prop])

        return props
