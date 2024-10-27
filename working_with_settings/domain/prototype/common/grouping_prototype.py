from itertools import groupby

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper


class GroupingPrototype:
    @staticmethod
    def group(data: list, groups: list[str]) -> list:
        return groupby(data, lambda x: tuple(GroupingPrototype._get_property(x, group) for group in groups))

    @staticmethod
    def _get_property(model, group: str):
        item_dict = AbsoluteMapper.to_dict(model)

        keys_array = group.split('.')

        inner_value = item_dict

        for key in keys_array:
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False

        return inner_value
