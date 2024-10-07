import enum


class EnumMeta(enum.EnumMeta):
    def __contains__(cls, item):
        return isinstance(item, cls) or item in [v.name for v in cls.__members__.values()]
