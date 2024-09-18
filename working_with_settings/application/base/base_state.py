from copy import deepcopy


class BaseState:
    def __init__(self):
        self._error = None

    @property
    def error(self):
        return self._error

    def with_error(self, value: Exception):
        state = deepcopy(self)
        state._error = value
        return state
