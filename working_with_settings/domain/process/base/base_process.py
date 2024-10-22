from abc import abstractmethod, ABC
from typing import TypeVar, Generic

INPUT = TypeVar('INPUT')
RESULT = TypeVar('RESULT')


class BaseProcess(Generic[INPUT, RESULT], ABC):
    @abstractmethod
    def calculate(self, inp: INPUT) -> RESULT:
        raise NotImplementedError('calculate() not implemented')
