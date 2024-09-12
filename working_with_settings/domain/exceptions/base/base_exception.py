class AppException(Exception):
    def __init__(self, message: str):
        self._message = ''
        self.message = message.strip()

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str):
        if not isinstance(value, str):
            raise TypeError('message must be str')
        self._message = value

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
