from abc import ABC
from dataclasses import dataclass

from core.domain.values.base import Id


@dataclass(eq=False)
class BsEntity(ABC):
    id: Id