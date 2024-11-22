from dataclasses import dataclass as datacls

from core.domain.values.base import BsValue, VT


@datacls(frozen=True)
class MsgRole(BsValue[VT]):
    value: VT

    def validate(self) -> None:
        ...

    def as_generic_type(self) -> str:
        return str(self.value)


@datacls(frozen=True)
class MsgContent(BsValue[VT]):
    value: VT

    def validate(self) -> None:
        ...

    def as_generic_type(self) -> str:
        return str(self.value)