from working_with_settings.domain.exceptions.base.base_exception import ArgumentException


class InvalidLengthException(ArgumentException):
    def __init__(self, waited: int, actual: int):
        super().__init__('Invalid length. Waited {}, actual {}'.format(waited, actual))


class InvalidTypeException(ArgumentException):
    def __init__(self, waited: type, actual: type):
        super().__init__('Invalid type. Waited {}, actual {}'.format(waited, actual))


class InvalidFormatException(ArgumentException):
    def __init__(self, waited: str, actual: str):
        super().__init__('Invalid format. Waited {}, actual {}'.format(waited, actual))
