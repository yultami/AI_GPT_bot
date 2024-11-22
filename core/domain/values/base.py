from abc import ABC, abstractmethod as abstract
from dataclasses import dataclass as datacls
from typing import TypeVar, Any, Generic

VT = TypeVar('VT', bound=Any)


@datacls(frozen=True)
class BsValue(ABC,Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstract
    def validate(self) -> None:
        ...

    @abstract
    def as_generic_type(self) -> VT:
        ...


@datacls(frozen=True)
class Id(BsValue[int]):
    value: int

    def __str__(self):
        return str(self.value)

    def validate(self) -> None:
        ...

    def as_generic_type(self) -> int:
        return int(self.value)