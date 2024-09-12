from working_with_settings.domain.exceptions.base.base_exception import AppException


class InvalidLengthException(AppException):
    def __init__(self, waited: int, actual: int):
        super().__init__('Invalid length. Waited {}, actual {}'.format(waited, actual))


class InvalidTypeException(AppException):
    def __init__(self, waited: type, actual: type):
        super().__init__('Invalid type. Waited {}, actual {}'.format(waited, actual))


class InvalidFormatException(AppException):
    def __init__(self, waited: str, actual: str):
        super().__init__('Invalid format. Waited {}, actual {}'.format(waited, actual))
