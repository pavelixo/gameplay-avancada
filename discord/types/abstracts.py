from abc import ABC
from typing import TypeVar, Generic

T = TypeVar('T')


class AbstractTypes(ABC, Generic[T]):
    def __init__(self, value: T):
        self.value = value


class Endpoint(AbstractTypes[str]):
    pass


class ID(AbstractTypes[int]):
    pass


class Data(AbstractTypes[dict]):
    pass