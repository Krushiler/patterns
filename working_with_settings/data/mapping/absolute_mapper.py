from working_with_settings.domain.model.base.base_model import BaseModel
from typing import get_type_hints


class AbsoluteMapper:
    _primitives = (bool, str, int, float, type(None))

    @staticmethod
    def from_dict(dictionary: dict | object, cls: type):
        if dictionary is None:
            return None
        if cls in AbsoluteMapper._primitives:
            return dictionary

        obj = cls.__new__(cls, cls)

        class_fields = get_type_hints(obj)

        if isinstance(obj, BaseModel):
            class_fields['_id'] = str

        for field in dictionary.keys():
            type_hint_name = f'_{field}'

            if type_hint_name not in class_fields.keys():
                continue

            setattr(obj, field, AbsoluteMapper.from_dict(dictionary[field], class_fields[type_hint_name]))

        return obj

    @staticmethod
    def to_dict(obj) -> dict:
        def get_properties(obj):
            return dict(
                (x, getattr(obj, x)) for x in obj.__class__.__dict__ if
                isinstance(obj.__class__.__dict__[x], property))

        props = get_properties(obj)

        if isinstance(obj, BaseModel):
            props['id'] = obj.id

        for prop in props:
            if isinstance(props[prop], list):
                new_list = []
                for item in props[prop]:
                    new_list.append(AbsoluteMapper.to_dict(item))
                props[prop] = new_list
            elif hasattr(props[prop], '__dict__'):
                props[prop] = AbsoluteMapper.to_dict(props[prop])

        return props
