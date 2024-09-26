from working_with_settings.domain.model.base.base_model import BaseModel


class AbsoluteMapper:
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
