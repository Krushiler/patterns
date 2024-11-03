from itertools import groupby

from working_with_settings.data.mapping.absolute_mapper import AbsoluteMapper


class GroupingPrototype:
    @staticmethod
    def group(data: list, groups: list[str], value_to_group: str = None) -> list:
        return groupby(data,
                       lambda x: tuple(GroupingPrototype._get_property(x, group, value_to_group) for group in groups))

    @staticmethod
    def _get_property(model, group: str, value_to_group: str = None):
        item_dict = AbsoluteMapper.to_dict(model)

        keys_array = group.split('.')

        inner_value = item_dict

        if value_to_group is not None:
            inner_value = inner_value.get(value_to_group, None)
            if inner_value is None:
                return False

        for key in keys_array:
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False

        return inner_value
